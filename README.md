# Leman FENG — personal website

Public source repository for the personal site formerly hosted on WordPress at lemanfeng.com.

## Maintenance

- Edit `content/pages.json` for restored project descriptions.
- Edit `scripts/build.py` for the homepage, About page and shared HTML.
- Edit `dist/style.css` for styling; `dist/assets/` preserves the original project images and animated GIFs.
- Run `python3 scripts/build.py` to generate the static pages.
- Serve `dist/` locally or on any static host. No PHP, database, npm dependencies or credentials are required.

## Hosting

The production target is GitHub Pages. `.github/workflows/pages.yml` builds and publishes `dist/` on every push to `main`. `scripts/pages-paths.py` adjusts links for the project URL and automatically uses root paths when a custom domain is configured. No deployment credentials need to be stored in the repository.

The earlier Sites deployment remains available during migration. `.openai/hosting.json` records that existing deployment's identity; its project ID is not a credential. GitHub Pages is the automatic publishing workflow going forward.

## Migration

Source: UpdraftPlus backup dated 2021-07-05 in the owner's Google Drive. The published project pages and all 47 referenced images/GIFs were preserved. Legacy `/index.php/<slug>/` paths redirect to their static equivalents. The old Resume Builder plugin pages now lead to the current professional About page; the complete private CV has not been published. Original WordPress drafts, revisions, user records, password hashes, SQL backups and server configuration are excluded.

`lemanfeng.com` DNS has not yet been switched. Custom-domain configuration is a separate step after the public site is verified.
