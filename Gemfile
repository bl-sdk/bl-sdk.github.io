source "https://rubygems.org"

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!
gem "jekyll", "~> 3.9.3"

# This is the default theme for new Jekyll sites. You may change this to anything you like.
# gem "minima", "~> 2.0"
gem "just-the-docs", "~> 0.10.0"

# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
# gem "github-pages", group: :jekyll_plugins

# If you have any plugins, put them here!
group :jekyll_plugins do
  # We can't use github pages directly since it forces safe mode, so I went through the list and
  # these seem to be it's useful dependencies
  gem 'jekyll-commonmark-ghpages', '~> 0.4.0'
  gem 'jekyll-default-layout', '~> 0.1.5'
  gem 'jekyll-include-cache', '~> 0.2.1'
  gem 'jekyll-optional-front-matter', '~> 0.3.2'
  gem 'jekyll-relative-links', '~> 0.7.0'
  gem 'jekyll-seo-tag', '~> 2.8'
  gem 'jekyll-sitemap', '~> 1.4'
  gem 'jekyll-titles-from-headings', '~> 0.5.3'

  gem "jekyll-redirect-from", "~> 0.16.0"
  gem "perfect_toml", "~> 0.9.0"
end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.0", :install_if => Gem.win_platform?

# kramdown v2 ships without the gfm parser by default. If you're using
# kramdown v1, comment out this line.
gem "kramdown-parser-gfm"

# Lock `http_parser.rb` gem to `v0.6.x` on JRuby builds since newer versions of the gem
# do not have a Java counterpart.
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]

gem "webrick", :require => false
gem "html-proofer", :require => false
gem "logger", :require => false
gem "csv", :require => false
