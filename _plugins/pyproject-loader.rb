require "net/http"
require "perfect_toml"

Jekyll::Hooks.register :documents, :pre_render do |doc|
    if doc.collection.label != "mods" then
        next
    end

    if !doc.data.key?("pyproject_url") then
        Jekyll.logger.error("#{doc.path}: no pyproject url")
        next
    end

    pyproject_url = doc.data["pyproject_url"]

    url = pyproject_url
    redirects = 10
    begin
        resp = Net::HTTP.get_response(URI.parse(url))
        url = resp["location"]
        redirects -= 1
    end while resp.is_a?(Net::HTTPRedirection) && redirects > 0

    if !resp.is_a?(Net::HTTPSuccess) then
        Jekyll.logger.error("#{doc.path}: failed to download pyproject: #{resp.code}")
        next
    end

    doc.data['pyproject'] = PerfectTOML.parse(resp.body)
end
