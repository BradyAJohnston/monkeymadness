# Example repo for an example add-on!

Subscribe to this add-on here:

```
https://bradyajohnston.github.io/monkeymadness/index.json
```

Run these build commands to re-build your add-on and the 'extension repo'. Push the changes to GitHub and wait for the website to update.

## Build Script
```bash
blender --command extension build --source-dir monkeymadness
blender --command extension server-generate --repo-dir . --html
```
