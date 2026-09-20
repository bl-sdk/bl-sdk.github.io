class CategoryPageGenerator < Jekyll::Generator
  safe true

  def generate(site)
    if !(site.config["category_index"] || {})["enabled"] then
      return
    end

    # It turns out the normal tag/category system only applies to *posts*, not all pages
    # Instead, we have to reimplement its logic, but do it for everything
    @mod_categories = Hash.new { |hash, key| hash[key] = [] }

    site.collections.each_value do |collection|
      collection.docs.each do |document|
        collect_categories(document)
      end
    end
    site.pages.flatten.each do |page|
      collect_categories(page)
    end

    if @mod_categories.empty? then
      return
    end

    site.pages << CategoryList.new(site, @mod_categories.keys())
    @mod_categories.each do |category, pages|
      site.pages << CategoryIndex.new(site, category, pages)
    end
  end

  def collect_categories(page)
    (page.data["mod_categories"] || "").split().reject { |cat| cat.empty? }.each do |cat|
      @mod_categories[cat.downcase] << page
    end
  end
end

CATEGORY_LIST_TITLE = "Browse Mod Categories"

class CategoryList < Jekyll::Page
  def initialize(site, categories)
    @site     = site
    @base     = site.source
    @dir      = site.config["category_index"]["url"]
    @basename = "index"
    @ext      = ".html"
    @name     = "index.html"
    @data = {
      "all_categories" => categories,
      # Get it to appear at the bottom of the sidebar
      "title" => CATEGORY_LIST_TITLE,
      "nav_order" => 999,
    }
    data.default_proc = proc do |_, key|
      site.frontmatter_defaults.find(relative_path, :category_list, key)
    end
  end
end

class CategoryIndex < Jekyll::Page
  def initialize(site, category, pages)
    @site     = site
    @base     = site.source
    @dir      = site.config["category_index"]["url"] + category
    @basename = "index"
    @ext      = ".html"
    @name     = "index.html"
    @data = {
      "mod_category" => category,
      "mods" => pages,
      # Make it appear in the sidebar, under the root
      "title" => site.data["categories"].fetch(category, {})["title"] || category,
      "parent" => CATEGORY_LIST_TITLE,
    }
    data.default_proc = proc do |_, key|
      site.frontmatter_defaults.find(relative_path, :category_index, key)
    end
  end
end

