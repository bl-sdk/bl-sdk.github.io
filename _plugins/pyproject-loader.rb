require "net/http"
require "perfect_toml"
require "liquid"

module PyProjectLoader
extend Liquid::StandardFilters

# We want to replace the title of each mod page with that loaded from the pyproject
# To make sure we do this early enough, we need to use a site hook
# Trying to do a hook on `:mods, :pre_render` would be more efficient, but leads to some bits of the
# site using the old title

Jekyll::Hooks.register :site, :post_read do |site|
    site.collections.each{|key, collection|
        if !key.end_with?("_mods")
            next
        end

        collection.docs.each{|mod|
            if mod.data.key?("legacy") then
                next
            end

            if !mod.data.key?("pyproject_url") then
                Jekyll.logger.error("#{mod.path}: no pyproject url")
                next
            end

            pyproject_url = mod.data["pyproject_url"]

            url = pyproject_url
            redirects = 10
            begin
                begin
                    resp = Net::HTTP.get_response(URI.parse(url))
                    url = resp["location"]
                    redirects -= 1
                end while resp.is_a?(Net::HTTPRedirection) && redirects > 0
            rescue => e
                Jekyll.logger.error("#{mod.path}: failed to download pyproject: #{e}")
                next
            end

            if !resp.is_a?(Net::HTTPSuccess) then
                Jekyll.logger.error("#{mod.path}: failed to download pyproject: #{resp.code}")
                next
            end

            pyproject = PerfectTOML.parse(resp.body)
            mod.data["pyproject"] = pyproject

            # Replace the title with that from the pyproject
            # Would prefer to handle this entirely from a layout, but unfortunately jekyl-seo-tag checks
            # page.title specifically, which we can't overwrite from one

            # Check if the front matter already contains a title, if so abort and just use that one
            if File.read(mod.path) =~ Jekyll::Document::YAML_FRONT_MATTER_REGEXP then
                front_matter = SafeYAML.load($1)
                if front_matter.key?("title") then
                    # Also mark a flag so we can pass this to the js later
                    mod.data["_title_from_frontmatter"] = true
                    next
                end
            else
                next
            end

            # Check `tool.sdkmod.name` then `project.name`
            mod_name = ((pyproject["tool"] || {})["sdkmod"] || {})["name"]
            mod_name ||= (pyproject["project"] || {})["name"] || ""
            mod_name = escape(mod_name.strip())
            if !mod_name.empty?() then
                mod.data["title"] = mod_name
            end
        }
    }
end

end
