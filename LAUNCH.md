# Launch and Google Search checklist

## Publish the site

- Push the source to your GitHub repository and connect it to your hosting provider.
- Publish `dist` as the public directory. Keep the paid ebook out of it.
- Attach `embroidhub.com` and configure DNS using the hosting provider’s actual values.
- Enable HTTPS and redirect HTTP and `www` to `https://embroidhub.com/`.
- Ensure the production site is public, returns HTTP 200, and has no authentication or `noindex` header. A private review URL cannot serve as the public SEO launch.
- Open the homepage on a phone and desktop. Test every purchase link through the Hotmart checkout without placing an order.
- Confirm the product, current price, delivery format and purchase terms in Hotmart match the offer. The landing page intentionally does not invent commercial terms.

## Submit to Google

1. Add `embroidhub.com` as a Domain property in Google Search Console.
2. Add Google's supplied verification TXT record to DNS. No verification token is included because none has been provided.
3. Submit `https://embroidhub.com/sitemap.xml`.
4. Use URL Inspection on `https://embroidhub.com/`, test the live URL and request indexing.
5. Check mobile usability and performance with PageSpeed Insights. Inspect structured data with Schema Markup Validator; Book markup does not guarantee a supported Google rich-result feature.
6. Monitor indexing, search queries, impressions, clicks and click-through rate. Adjust the page based on real queries and buyer questions rather than repeating keywords.

## What is already implemented

- English document language, one descriptive H1 and logical section headings.
- Useful, original introductory content plus a focused paid offer.
- Title, description, canonical address, Open Graph text metadata and favicon.
- Book, WebPage and WebSite JSON-LD with the supplied author and verified page count.
- Sitemap and robots.txt pointing to the intended production domain.
- Responsive CSS, keyboard focus states, a skip link and native FAQ disclosure controls.
- No JavaScript dependency, third-party fonts, trackers or exposed paid PDF.
- Explicit cover dimensions to reduce layout shifts, plus a high-priority hero image.

## What remains external

Domain/DNS setup, GitHub account access, public hosting, Search Console verification and submission, and checkout validation require the respective account access. These have not been represented as completed.

SEO improves discoverability; it cannot guarantee indexing, rankings or sales. Google may take time to crawl and evaluate a new site. Build relevant, legitimate links and continue improving the material based on real reader needs.

Sources:
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
