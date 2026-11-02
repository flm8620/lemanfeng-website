# Leman FENG — personal website

Public source repository for the personal site formerly hosted on WordPress at lemanfeng.com.

## Maintenance

- Edit `content/pages.json` for restored project descriptions.
- Edit `scripts/build.py` for the homepage and shared HTML.
- Edit `content/cv.html` for the photo-free web CV; keep its professional content aligned with the CV source. Replace `dist/CV_Leman_FENG_2026_CN.pdf` when the compiled PDF changes.
- Edit `dist/slideshow.js` for the ray-tracing slideshow.
- Edit `dist/style.css` for styling; `dist/assets/` preserves the original project images and animated GIFs.
- Run `python3 scripts/build.py` to generate the static pages.
- Serve `dist/` locally or on any static host. No PHP, database, npm dependencies or credentials are required.

## Hosting

The production URL is https://lemanfeng.com/ and the site is hosted by GitHub Pages. `.github/workflows/pages.yml` builds and publishes `dist/` on every push to `main`. `scripts/pages-paths.py` adjusts links for the project URL and automatically uses root paths when a custom domain is configured. No deployment credentials need to be stored in the repository.

The earlier Sites deployment remains available during migration. `.openai/hosting.json` records that existing deployment's identity; its project ID is not a credential. GitHub Pages is the automatic publishing workflow going forward.

## Migration

Source: UpdraftPlus backup dated 2021-07-05 in the owner's Google Drive. The published project pages and all 47 referenced images/GIFs were preserved, with full-resolution Day 1 and Day 2 images added for the slideshow. Legacy `/index.php/<slug>/` paths redirect to their static equivalents. The homepage shows all projects inline. The old Resume Builder plugin pages now lead to the photo-free web CV, and a compiled PDF download is also published at the owner’s request. Original WordPress drafts, revisions, user records, password hashes, SQL backups and server configuration are excluded.

`lemanfeng.com` and `www.lemanfeng.com` DNS point to GitHub Pages. After changing the custom domain in Pages settings, run the publishing workflow again so its configured base path is reflected in all links and assets. Enable Enforce HTTPS after certificate provisioning completes.

## Paper demonstration video

The CODT project uses `dist/assets/codt-3d-bimba.mp4`, a web-optimized copy of `TheMakingOfBimba.mp4` from the authors’ supplementary archive at https://geometry.caltech.edu/pubs/FABDD18_supp.zip (paper DOI: https://doi.org/10.1145/3197517.3201358). The complete 39-second video retains its audio and is encoded as H.264/AAC with fast-start metadata for browser playback. Its companion homepage item is the original `untangling.gif`.
