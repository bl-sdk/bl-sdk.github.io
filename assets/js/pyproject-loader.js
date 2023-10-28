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
        document.querySelector("#authors").innerText = arr_to_sentence(authors);
    }

    if (fields?.version) {
        const version = pyproject?.tool?.sdkmod?.version || pyproject?.project?.version;
        if (version) {
            document.querySelector("#version").innerText = version;
        }
    }

    if (fields?.games) {
        const ALLOWED_GAMES = ["BL3", "WL"];
        const game_list = pyproject?.tool?.sdkmod?.supported_games || ALLOWED_GAMES;
        const games = arr_to_sentence(game_list.filter(x => ALLOWED_GAMES.includes(x)));
        if (games) {
            document.querySelector("#games").innerText = games;
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
}

export { load_from_pyproject }
