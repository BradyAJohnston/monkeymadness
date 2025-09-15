# Example repo for an example add-on!

Subscribe to this add-on here:

```
https://bradyajohnston.github.io/monkeymadness/index.json
```

Runt this build script before pushing to the repo to update the add-on.

## Build Script
```bash
blender --command extension build --source-dir monkeymadess
blender --command extension server-generate --repo-dir . --html
```
