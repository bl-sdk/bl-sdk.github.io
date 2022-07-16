---
layout: main
modTypes: ['Utility', 'Gameplay', 'Content', 'Library'] # Defines all of the mods that we want to be shown in terms of categories
---

**Page Contents**
* TOC
{:toc}

This page has a list of PythonSDK mods, and what games they support!
If you want to see more information on how to install these mods, go see the [Installation Guide](/#mod-installation)

<p style="margin-left: 25%">
{% for modType in page.modTypes %}
    <span class="modTypeButton"><a href="/types/{{modType}}" class="none">{{modType}}</a></span>
{% endfor %}
</p>

## All Mods

{% for mod in site.mods %}

* [{{ mod.title }}]({{ site.baseurl }}{{ mod.url }}) by {{mod.authors}} (Version: {{mod.version}})
    - Description: {{mod.tagline}}
    - Supports: `{{mod.supported}}`
    - Types: {{ mod.categories | array_to_sentence_string }}
<br>

{% endfor %}
