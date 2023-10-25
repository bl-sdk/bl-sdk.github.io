class YouTube < Liquid::Tag
    # Original regex taken from https://stackoverflow.com/a/37704433
    URL_REGEX = /^(?:(?:https?:)?\/\/)?(?:(?:www|m)\.)?(?:(?:youtube\.com|youtu.be))?(?:\/(?:[\w\-]+\?v=|embed\/|v\/)?)?([\w\-]+)(?:[\?\&](\S+))?\s*$/

    def initialize(tagName, url, tokens)
        super

        if url =~ URL_REGEX then
            @id = $1
            @query = $2
        else
            raise Failed to parse video url
        end
    end

    def render(context)
        %{<div class="video-16-9">
            <iframe
                src="https://www.youtube.com/embed/#{@id}?#{@query}"
                frameborder="0"
                allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen
            ></iframe>
        </div>}
    end

    Liquid::Template.register_tag("youtube", self)
end
