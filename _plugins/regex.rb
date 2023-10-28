module Regex
    def regex_replace(str, pattern, value, options = "im")
        return str.gsub(Regexp.new(pattern, options), value)
    end

    def regex_match(str, pattern, idx = 0, options = "im")
        return str.match(Regexp.new(pattern, options))[idx]
    end
end

Liquid::Template.register_filter(Regex)
