# Leman FENG — personal website

Private source repository for the public personal site formerly hosted on WordPress at lemanfeng.com.

## Maintenance

- Edit `content/pages.json` for restored project descriptions.
- Edit `scripts/build.py` for the homepage, About page and shared HTML.
- Edit `dist/style.css` for styling; `dist/assets/` preserves the original project images and animated GIFs.
- Run `python3 scripts/build.py` to generate the static pages.
- Serve `dist/` locally or on any static host. No PHP, database, npm dependencies or credentials are required.

## Hosting

The site is published with Sites; the project identity is in `.openai/hosting.json`. GitHub is private source storage. GitHub Pages is not enabled because the current GitHub plan does not support Pages from private repositories. Changes in this repository do **not** automatically deploy: the maintainer must synchronize the source to the Sites repository and publish a matching saved version with the Sites workflow. Keep both sources consistent after changes.

## Migration

Source: UpdraftPlus backup dated 2021-07-05 in the owner's Google Drive. The published project pages and all 47 referenced images/GIFs were preserved. Legacy `/index.php/<slug>/` paths redirect to their static equivalents. The old Resume Builder plugin pages now lead to the current professional About page; the complete private CV has not been published. Original WordPress drafts, revisions, user records, password hashes, SQL backups and server configuration are excluded.

`lemanfeng.com` DNS has not yet been switched. Custom-domain configuration is a separate step after the public site is verified.
