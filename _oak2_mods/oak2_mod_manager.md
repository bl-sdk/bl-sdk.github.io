---
pyproject_url: https://raw.githubusercontent.com/bl-sdk/oak2-mod-manager/master/manager_pyproject.toml
version: Unknown
nav_exclude: true
---
<script>
async function update_version() {
    const response = await fetch(
        "https://api.github.com/repos/bl-sdk/oak2-mod-manager/releases/latest",
        {
            headers: {
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        }
    );
    const data = await response.json();
    if (data.tag_name) {
        document.querySelector("#version").innerText = data.tag_name;
    }
}
document.extra_custom_updater_promises = [update_version()];
</script>

The SDK itself.
