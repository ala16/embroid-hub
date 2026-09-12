# Mastering Mandarin Tones — EmbroidHub

A complete English-language sales landing page for Ricardo Rodrigues Filho’s ebook. Built with plain HTML and CSS, with no dependencies, build step, trackers or form backend. All purchase calls to action point to https://go.hotmart.com/N101596432X.

## Files

- `dist/index.html`: page copy, semantic structure, metadata and Book structured data.
- `dist/assets/styles.css`: responsive layout, focus styles and reduced-motion support.
- `dist/assets/ebook-cover.png`: supplied book cover.
- `dist/robots.txt` and `dist/sitemap.xml`: crawling and sitemap configuration.
- `LAUNCH.md`: publishing and search launch checklist.

The paid PDF is deliberately excluded from this repository and the public website. Only the supplied cover and an original introductory lesson are published.

## Preview

Open `dist/index.html` in a browser, or serve the `dist` directory with any local static server. The site works without JavaScript. Expand the FAQ items to view their answers.

## Export to GitHub

1. Create an empty GitHub repository under your account.
2. Upload this folder’s contents, keeping `dist` and its subfolders intact. Do not upload the ZIP itself or the paid PDF.
3. Connect the repository to a static hosting provider that permits commercial landing pages, such as Cloudflare Pages or Netlify, subject to its current terms.
4. Select no framework, leave the build command empty, and set the publish/output directory to `dist`. A `netlify.toml` file is included for Netlify.
5. Add `embroidhub.com` in the hosting provider’s custom domain settings and follow the exact DNS instructions it supplies. Enable HTTPS.

GitHub is the source repository. The GitHub Pages service has restrictions on sites primarily facilitating commercial transactions; do not assume it is an appropriate storefront host. See https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits.

If you use Git locally, run these commands from this project folder after replacing the repository URL:

```sh
git init
git add .
git commit -m "Add Mandarin tones landing page"
git branch -M main
git remote add github https://github.com/YOUR-ACCOUNT/YOUR-REPOSITORY.git
git push -u github main
```

If the folder already contains a Git repository, skip initialization and the first commit when there are no changes. No GitHub repository has been created or connected on your behalf.

The `.openai/hosting.json` file is only for the separate Sites review deployment. It is not required for hosting from GitHub; the public output is `dist`. `CNAME` and `.nojekyll` are inert compatibility files on hosts that do not use them; the CNAME file alone never configures DNS.

## Content and SEO

The canonical production address is `https://embroidhub.com/`. Update the canonical, Open Graph URL, JSON-LD URLs, robots sitemap address and sitemap together if the production URL changes. Pinyin appears only as instructional examples; the page interface and explanatory content are in English.

The page targets natural search intent around Mandarin tones for English speakers, the four Mandarin tones, pronunciation, the neutral tone, second vs. third tone and tone sandhi. It uses a single H1, descriptive headings, readable HTML, an optimized local cover, a favicon, descriptive metadata and Book structured data. No invented reviews, sales figures, credentials, price, discount, guarantee or audio bundle are included. Book schema describes the product; it does not promise Google rich results.

The actual checkout price and delivery terms remain on Hotmart. The supplied purchase URL was preserved exactly; validate its final destination before launch.

## Editing

Edit the English text directly in `dist/index.html`. Replace all Hotmart links together if the purchase link changes. Edit the color tokens at the top of `dist/assets/styles.css` to adjust the palette. If adding analytics, forms or cookies later, implement appropriate disclosures and controls for the actual processing involved.

Reference: https://developers.google.com/search/docs/fundamentals/seo-starter-guide

