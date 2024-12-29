---
---
import { parse as parse_toml } from "https://cdn.jsdelivr.net/npm/smol-toml@1.1.3/+esm"

function arr_to_sentence(arr) {
    switch (arr.length) {
        case 0:
            return "";
        case 1:
        case 2:
            return arr.join(" and ");
        default:
            return arr.slice(0, -1).join(", ") + ", and " + arr[arr.length - 1];
    }
}

function make_link(name, url) {
    const link = document.createElement("a");
    link.innerText = name;
    link.href = url;
    return link;
}

function strip_decode_html(input) {
   return new DOMParser().parseFromString(input, 'text/html').body.textContent || "";
}

async function load_from_pyproject(url, fields) {
    const response = await fetch(url);
    if (!response.ok) {
        throw `failed to fetch pyproject: ${response.statusText} (from ${url})`
    }

    const pyproject = parse_toml(await response.text());
    window.pyproject = pyproject;

    if (fields?.title) {
        const title = pyproject?.tool?.sdkmod?.name || pyproject?.project?.name;
        if (title) {
            document.querySelector("#title").innerText = title;
        }
    }

    if (fields?.authors) {
        const authors = (pyproject?.project?.authors || []).map(x => x.name);
        if (authors) {
            document.querySelector("#authors").innerText = arr_to_sentence(authors);
        }
    }

    if (fields?.version) {
        const version = pyproject?.tool?.sdkmod?.version || pyproject?.project?.version;
        if (version) {
            document.querySelector("#version").innerText = version;
        }
    }

    if (fields?.games) {
        const ALLOWED_GAMES = {
            "willow2": {"BL2": "BL2", "TPS": "TPS", "AODK": "AoDK"},
            "oak": {"BL3": "BL3", "WL": "WL"},
        }[window.location.pathname.match(/^\/(willow2|oak)-mod-db/)[1]];

        const game_list = pyproject?.tool?.sdkmod?.supported_games || Object.keys(ALLOWED_GAMES);
        const filtered_games = [...new Set(game_list.filter(x => x.toUpperCase() in ALLOWED_GAMES)
                                                    .map(x => ALLOWED_GAMES[x.toUpperCase()]))];
        if (filtered_games) {
            document.querySelector("#games").innerText = arr_to_sentence(filtered_games);
        }
    }

    if (fields?.coop) {
        const coop_support = pyproject?.tool?.sdkmod?.coop_support;
        if (coop_support) {
            const COOP_SUPPORT_TO_FRIENDLY_NAME = {
                "incompatible": "Incompatible",
                "requiresallplayers": "Requires All Players",
                "clientside": "Client Side",
            };
            const friendly = COOP_SUPPORT_TO_FRIENDLY_NAME[coop_support.toLowerCase()] || "Unknown";
            document.querySelector("#coop").innerText = friendly;
        }
    }

    if (fields?.license) {
        const license_element = document.querySelector("#license");

        const sdkmod_license = pyproject?.tool?.sdkmod?.license;
        if (sdkmod_license?.name && sdkmod_license?.url) {
            license_element.replaceChildren(make_link(sdkmod_license.name, sdkmod_license.url));
        } else {
            const project_license = pyproject?.project?.license?.text;
            if (project_license) {
                license_element.innerText = project_license;
            }
        }
    }

    if (fields?.dependencies) {
        const DEPENDENCY_DATA = {
            {%- assign first = true -%}
            {%- for mod in site.mods -%}
            {%- if mod.pyproject.project.name -%}
                {%- unless first -%},{%- endunless -%}
                {%- assign first = false -%}

                {{- mod.pyproject.project.name | jsonify -}}:{
{{-""-}}            title: {{- mod.title | decode | jsonify -}},
{{-""-}}            url: {{- mod.url | relative_url | jsonify -}}
                }
            {%- endif -%}
            {%- endfor -%}
        };

        const dependencies = pyproject?.project?.dependencies;
        if (dependencies) {
            let insert_point = document.querySelector("dt.requirement");
            if (insert_point) {
                // Delete existing data entries
                document.querySelectorAll("dd.requirement").forEach(x => x.remove());
            } else {
                // Create a new header
                insert_point = document.createElement("dt");
                insert_point.classList.add("requirement");
                insert_point.innerText = "Requires";
                document.querySelector("#license").after(insert_point);
            }

            dependencies.forEach(dependency => {
                const name = dependency.match(/^\s*([A-Z0-9][A-Z0-9._-]*[A-Z0-9]|[A-Z0-9])/i)[0];

                const entry = document.createElement("dd");
                entry.classList.add("requirement");

                if (name in DEPENDENCY_DATA) {
                    const info = DEPENDENCY_DATA[name];
                    // Titles will be html encoded, decode them
                    const title = strip_decode_html(info.title);
                    const url = info.url;
                    entry.appendChild(make_link(title, url));
                } else {
                    const span = document.createElement("span");
                    span.innerText = name;
                    entry.appendChild(span);
                }

                const div = document.createElement("div");
                const code = document.createElement("code");
                code.classList.add("language-plaintext", "highlighter-rouge");
                code.innerText = dependency;

                div.appendChild(code);
                entry.appendChild(div);

                insert_point.after(entry);
                insert_point = entry;
            });
        // If `pyproject.project` exists, but `pyproject.project.dependencies` does not/is empty
        } else if (pyproject?.project) {
            // Remove all dependency fields
            document.querySelectorAll(".requirement").forEach(x => x.remove());
        }
    }

    if (fields?.urls) {
        let url_box = document.querySelector("div.mod-url-box");

        const urls = pyproject?.project?.urls;
        if (urls) {
            const new_children = Object.entries(urls).map(([name, url]) => make_link(name, url));

            if (new_children.length > 0){
                if (!url_box) {
                    url_box = document.createElement("div");
                    url_box.classList.add("mod-url-box");
                    document.querySelector("dl.mod-desc").after(url_box);
                }

                url_box.replaceChildren(...new_children);

            // If `pyproject.project.urls` exists, but is empty
            } else {
                url_box?.remove();
            }


        // If `pyproject.project` exists, but `pyproject.project.urls` does not
        } else if (pyproject?.project) {
            url_box?.remove();
        }
    }

    if (fields?.download) {
        const download_url = pyproject?.tool?.sdkmod?.download;
        if (download_url) {
            let download_a = document.querySelector("#download");
            if (!download_a) {
                const insert_point = (document.querySelector("div.mod-url-box")
                                    || document.querySelector("dl.mod-desc"));

                insert_point.after(document.createElement("br"));

                download_a = document.createElement("a");
                download_a.id = "download";
                download_a.classList.add("btn", "btn-primary", "fs-5");
                download_a.innerText = "Download";
                insert_point.after(download_a);
            }
            download_a.href = download_url;
        }
    }

    if (fields?.description) {
        const description = pyproject?.project?.description;
        if (description) {
            const description_div = document.querySelector("#description");
            const paragraph = document.createElement("p");

            // Strip html from the description to not show any tags meant for the mod
            // Set innerHTML so that newlines get converted like from the markdown (i.e. they don't)
            paragraph.innerHTML = strip_decode_html(description);

            description_div.innerHTML = "";
            description_div.appendChild(paragraph);
        }
    }

    // Allow mod pages to have custom updaters, which we'll wait on before removing the notification
    if (document.extra_custom_updater_promises) {
        await Promise.all(document.extra_custom_updater_promises);
    }

    // Finished updating, hide the notification
    document.querySelector("span.mod-update-notification").remove();
}

export { load_from_pyproject }
