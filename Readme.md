## Hosting the site locally
You can start by running the standard jekyll commands.
```sh
bundle install
bundle exec jekyll serve
```

However, as you'll notice this only builds the dev docs. The final site actually consists of three
seperate jekyll projects, with one set of interwoven source files, the developer docs being the
default. You can build the others by appending an extra config file:

```sh
bundle exec jekyll serve --config _config.yml,_config_willow2.yml
bundle exec jekyll serve --config _config.yml,_config_oak.yml
```

Alternatively, `_jekyll.py` provides simpler aliases for this, `_jekyll.py build willow`.

To build and merge the three sites, run `_jekyll.py merge`. This creates a new `_merged_site` dir.

You can then use your favourite http server to host this merged directory - e.g.
`python -m http.server -d _merged_site 4000`, `ruby -run -e httpd -- _merged_site -p 4000`
