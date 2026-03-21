# Academic Pages Theme Structure Documentation

## Overview
Academic Pages is a GitHub Pages template for personal and professional portfolio-oriented websites. It's based on the Minimal Mistakes Jekyll Theme and uses Jekyll with Markdown and YAML for content management.

---

## 1. MAIN DIRECTORIES AND STRUCTURE

### Core Content Collections
- **_publications** — Markdown files for academic publications/papers
- **_talks** — Markdown files for presentations, talks, and seminars
- **_teaching** — Markdown files for teaching experiences and courses
- **_posts** — Blog posts and news articles
- **_portfolio** — Portfolio/project showcase items

### Template and Configuration
- **_layouts** — HTML layouts that define how content is displayed (`.html` files)
- **_includes** — Reusable HTML snippets and components
- **_data** — YAML configuration files (navigation, author info, etc.)
- **_sass** — SCSS stylesheets for theming and customization
- **_drafts** — Draft posts (not published)

### Static Assets
- **assets** — Images, JavaScript, CSS, and other static files
- **files** — PDFs, documents, and downloadable files (served at `/files/`)
- **images** — Theme images and media files

### Supporting Directories
- **scripts** — Python/Jupyter scripts for generating content from external data (TSV/CSV)
- **markdown_generator** — Jupyter notebooks and Python scripts to bulk-generate markdown files
- **talkmap** — Python/Jupyter scripts for generating talk maps with geolocation

### Development
- **.devcontainer** — Development container configuration for VS Code
- **.github** — GitHub Actions workflows and CI/CD configuration

---

## 2. KEY FILES IN EACH DIRECTORY

### Root Level Critical Files
```
_config.yml              — Main Jekyll configuration file (PRIMARY CONFIG)
_config_docker.yml       — Alternative config for Docker deployments
Gemfile                  — Ruby gem dependencies
Gemfile.lock             — Locked versions of gems
README.md                — Repository documentation
LICENSE                  — MIT License
.gitignore               — Git ignore rules
docker-compose.yaml      — Docker Compose configuration
Dockerfile               — Docker image configuration
package.json             — Node.js dependencies (for asset compilation)
```

### _PAGES Directory Files (8-10 primary pages)
```
_pages/
├── 404.md                      — 404 error page
├── about.md                    — About/Home page
├── cv.md                       — Curriculum Vitae (Markdown format)
├── cv-json.md                  — Curriculum Vitae (JSON format)
├── publications.html           — Publications archive/list page
├── talks.html                  — Talks archive/list page
├── teaching.html               — Teaching archive/list page
├── portfolio.html              — Portfolio archive/list page
├── year-archive.html           — Blog posts archive by year
├── category-archive.html       — Archive pages by category
├── tag-archive.html            — Archive pages by tag
├── markdown.md                 — Markdown guide/reference page
├── sitemap.md                  — XML sitemap
├── terms.md                    — Terms and conditions
├── non-menu-page.md            — Example non-menu page
└── archive-layout-with-content.md  — Archive layout examples
```

### _LAYOUTS Directory Files
```
_layouts/
├── default.html            — Base layout for all pages
├── single.html             — Single page layout (posts, pages, publications, teaching)
├── talk.html               — Specialized layout for talks
├── archive.html            — Archive page layout
├── archive-taxonomy.html   — Taxonomy-based archive layout (categories/tags)
├── cv-layout.html          — Curriculum Vitae layout
├── splash.html             — Full-width splash layout
└── compress.html           — HTML compression layout
```

### _INCLUDES Directory Files (Major Components)
```
_includes/
├── head.html                   — HTML head section (meta tags, stylesheets)
├── masthead.html               — Navigation header
├── footer.html                 — Footer section
├── sidebar.html                — Sidebar container
├── author-profile.html         — Author profile sidebar widget
├── scripts.html                — JavaScript includes
├── analytics.html              — Analytics integration
├── comments.html               — Comments section (Disqus, Discourse, etc.)
├── social-share.html           — Social media sharing buttons
├── seo.html                    — SEO meta tags
├── breadcrumbs.html            — Breadcrumb navigation
├── pagination.html             — Pagination for archive pages
├── post-pagination.html        — Post-to-post navigation
├── read-time.html              — Reading time estimate display
├── toc.html                    — Table of contents
├── paginator.html              — Archive paginator
├── gallery.html                — Image gallery component
├── feature_row.html            — Feature row component
├── category-list.html          — Category list component
├── tag-list.html               — Tag list component
├── nav_list.html               — Navigation list component
├── archive-single.html         — Single archive item display
├── archive-single-talk.html    — Single talk archive item display
├── archive-single-cv.html      — Single CV archive item display
├── page__hero.html             — Hero section for pages
├── page__taxonomy.html         — Taxonomy display for pages
├── cv-template.html            — CV template component
├── comment.html                — Single comment display
├── browser-upgrade.html        — Browser upgrade notice
└── base_path.html              — Base path helper
```

### _DATA Directory Files
```
_data/
├── navigation.yml              — Main navigation menu (PRIMARY CONFIG)
└── comments/                   — Comments storage (if using staticman)
```

### _SASS Directory Structure
```
_sass/
├── minimal-mistakes/           — Theme SCSS files
│   ├── _variables.scss         — Color and spacing variables
│   ├── _base.scss              — Base styles
│   ├── _layout.scss            — Layout styles
│   ├── _archives.scss          — Archive page styles
│   ├── _buttons.scss           — Button styles
│   ├── _footer.scss            — Footer styles
│   ├── _masthead.scss          — Header/masthead styles
│   ├── _navigation.scss        — Navigation styles
│   ├── _tables.scss            — Table styles
│   ├── _utilities.scss         — Utility classes
│   └── ... (additional theme files)
└── minimal-mistakes.scss       — Main stylesheet
```

### ASSETS Directory Structure
```
assets/
├── css/                        — Compiled CSS files
├── js/                         — JavaScript files
│   ├── _main.js                — Main application JS
│   ├── plugins/                — JS plugins (jQuery plugins, etc.)
│   └── vendor/                 — Third-party vendor JS libraries
├── images/                     — Theme images
│   ├── themes/                 — Theme preview images
│   └── ... (icon graphics, etc.)
└── vendor/                     — Vendor assets
```

---

## 3. SAMPLE TEMPLATE FORMATS

### PUBLICATION TEMPLATE
**File:** `_publications/2009-10-01-paper-title-number-1.md`

```yaml
---
title: "Paper Title Number 1"
collection: publications
category: manuscripts
permalink: /publication/2009-10-01-paper-title-number-1
excerpt: 'This paper is about the number 1. The number 2 is left for future work.'
date: 2009-10-01
venue: 'Journal 1'
slidesurl: 'https://academicpages.github.io/files/slides1.pdf'
paperurl: 'https://academicpages.github.io/files/paper1.pdf'
bibtexurl: 'https://academicpages.github.io/files/bibtex1.bib'
citation: 'Your Name, You. (2009). &quot;Paper Title Number 1.&quot; <i>Journal 1</i>. 1(1).'
---

The contents above will be part of a list of publications, if the user clicks 
the link for the publication than the contents of section will be rendered as 
a full page, allowing you to provide more information about the paper for the reader. 
When publications are displayed as a single page, the contents of the above 
"citation" field will automatically be included below this section in a smaller font.
```

**Front Matter Fields:**
- `title` — Publication title
- `collection: publications` — Identifies as publication
- `category` — Publication type (manuscripts, conferences, books)
- `permalink` — URL slug
- `excerpt` — Brief description
- `date` — Publication date (YYYY-MM-DD)
- `venue` — Journal/Conference name
- `slidesurl` — URL to presentation slides (optional)
- `paperurl` — URL to paper PDF
- `bibtexurl` — URL to BibTeX citation (optional)
- `citation` — HTML formatted citation text

---

### TALK TEMPLATE
**File:** `_talks/2012-03-01-talk-1.md`

```yaml
---
title: "Talk 1 on Relevant Topic in Your Field"
collection: talks
type: "Talk"
permalink: /talks/2012-03-01-talk-1
venue: "UC San Francisco, Department of Testing"
date: 2012-03-01
location: "San Francisco, CA, USA"
---

This is a description of your talk, which is a markdown file that can be all 
markdown-ified like any other post. Yay markdown!
```

**Front Matter Fields:**
- `title` — Talk title
- `collection: talks` — Identifies as talk
- `type` — Type of presentation (Talk, Workshop, Keynote, etc.)
- `permalink` — URL slug
- `venue` — Venue/Institution name
- `date` — Talk date (YYYY-MM-DD)
- `location` — Location (City, Country)

---

### TEACHING TEMPLATE
**File:** `_teaching/2014-spring-teaching-1.md`

```yaml
---
title: "Teaching experience 1"
collection: teaching
type: "Undergraduate course"
permalink: /teaching/2014-spring-teaching-1
venue: "University 1, Department"
date: 2014-01-01
location: "City, Country"
---

This is a description of a teaching experience. You can use markdown like any 
other post.

Heading 1
=========

Heading 2
=========

Heading 3
=========
```

**Front Matter Fields:**
- `title` — Course/Teaching title
- `collection: teaching` — Identifies as teaching
- `type` — Type (Undergraduate course, Graduate course, Seminar, etc.)
- `permalink` — URL slug
- `venue` — Institution name
- `date` — Start date (YYYY-MM-DD)
- `location` — Location (City, Country)

---

### BLOG POST TEMPLATE
**File:** `_posts/YYYY-MM-DD-post-title.md`

```yaml
---
title: "Blog Post Title"
date: 2024-01-01
collection: posts
layout: single
author_profile: true
read_time: true
comments: true
share: true
related: true
---

Blog post content in markdown format.
```

**Front Matter Fields:**
- `title` — Post title
- `date` — Publication date (YYYY-MM-DD)
- `layout: single` — Single page layout
- `author_profile: true` — Show author profile sidebar
- `read_time: true` — Show estimated reading time
- `comments: true` — Enable comments
- `share: true` — Show social sharing buttons

---

### PAGE TEMPLATE
**File:** `_pages/about.md`

```yaml
---
permalink: /
title: "About me"
excerpt: "This is a sample About page."
author_profile: true
redirect_from: 
  - about.html
---

Page content in markdown format.
```

---

## 4. _CONFIG.YML STRUCTURE AND KEY OPTIONS

### Location: Root `_config.yml`

### Site Basics
```yaml
# Locale and Language
locale: "en-US"

# Site Title and Name
title: "Your Name / Site Title"
title_separator: "-"
name: &name "Your Name"
description: &description "Your Name's academic portfolio"

# Site URL and Repository
url: "https://academicpages.github.io"
baseurl: ""  # Leave empty unless using subdirectory
repository: "academicpages/academicpages.github.io"

# Theme Selection
site_theme: "default"  # Options: "default", "air", "sunrise", "mint", "dirt", "contrast"
```

### Site Author/Profile Information
```yaml
author:
  # Biographic Information
  avatar: "profile.png"
  name: "Your Sidebar Name"
  pronouns: "she/her"  # or "he/him", "they/them", etc.
  bio: "Short biography for the left-hand sidebar"
  location: "Earth"
  employer: "Red Brick University"
  uri: ""  # Personal website URL
  email: "none@example.org"
  
  # Academic Profiles
  academia: ""  # academia.edu URL
  arxiv: ""  # arxiv profile
  googlescholar: "https://scholar.google.com/citations?user=PS_CX0AAAAAJ"
  inspire-hep: ""
  impactstory: ""
  orcid: "https://orcid.org/yourorcidurl"
  semantic: ""
  ssrn: ""
  pubmed: "https://www.ncbi.nlm.nih.gov/pubmed/?term=john+snow"
  researchgate: ""
  scopus: ""
  zotero: ""
  
  # Repositories and Development
  bitbucket: ""
  codepen: ""
  dribbble: ""
  github: "academicpages"
  kaggle: ""
  stackoverflow: ""
  
  # Social Media
  artstation: ""
  bluesky: ""  # Replace with Bluesky username
  facebook: ""
  flickr: ""
  foursquare: ""
  goodreads: ""
  google_plus: ""
  keybase: ""
  instagram: ""
  lastfm: ""
  linkedin: ""
  mastodon: ""  # Include @domain
  medium: ""
  pinterest: ""
  soundcloud: ""
  steam: ""
  telegram: ""
  tumblr: ""
  twitter: ""  # X/Twitter username
  vine: ""
  weibo: ""
  wikipedia: ""
  xing: ""
  youtube: ""
  zhihu: ""

# Publication Categories
publication_category:
  books:
    title: 'Books'
  manuscripts:
    title: 'Journal Articles'
  conferences:
    title: 'Conference Papers'
```

### Site Settings
```yaml
teaser: ""  # Teaser image for social media (place in /images/)
breadcrumbs: false  # true or false
words_per_minute: 160  # For read time calculation
future: true  # Publish posts with future dates
read_more: "disabled"  # "disabled" or show "Read more" links
talkmap_link: false  # true to add link to talkmap on talks page
```

### Comments Configuration
```yaml
comments:
  provider: false  # false, "disqus", "discourse", "facebook", "google-plus", "staticman", "custom"
  disqus:
    shortname: ""  # Disqus shortname
  discourse:
    server: ""  # e.g., meta.discourse.org
  staticman:
    allowedFields: ['name', 'email', 'url', 'message']
    branch: "gh-pages"
    commitMessage: "New comment."
    filename: "comment-{@timestamp}"
    format: "yml"
    moderation: true
    path: "_data/comments/{options.slug}"
    requiredFields: ['name', 'email', 'message']
```

### Analytics Configuration
```yaml
analytics:
  provider: false  # false, "google", "google-universal", "google-analytics-4", "custom"
  google:
    tracking_id: ""  # UA-XXXXXXXX-X or G-XXXXXXX
```

### SEO and Social
```yaml
# Search Engine Verification
google_site_verification: ""
bing_site_verification: ""
alexa_site_verification: ""
yandex_site_verification: ""

# Social Media
twitter:
  username: ""  # &twitter variable

facebook:
  username: ""
  app_id: ""
  publisher: ""

og_image: ""  # Open Graph image path
og_description: ""  # Open Graph description

# Social Profiles for structured data
social:
  type: "Person"  # Person or Organization
  name: ""  # If different from site name
  links: []  # Array of social profile URLs
```

### File Includes/Excludes
```yaml
include:
  - .htaccess
  - _pages
  - files

exclude:
  - "*.sublime-project"
  - "*.sublime-workspace"
  - .asset-cache
  - .bundle
  - .github
  - .jekyll-assets-cache
  - .sass-cache
  - node_modules
  - Gemfile
  - Gruntfile.js
  - LICENSE
  - README
  - vendor

keep_files:
  - .git
  - .svn

encoding: "utf-8"
markdown_ext: "markdown,mkdown,mkdn,mkd,md"
```

### Markdown and Code Highlighting
```yaml
markdown: kramdown
highlighter: rouge
lsi: false
excerpt_separator: "\n\n"
incremental: false

kramdown:
  input: GFM
  hard_wrap: false
  auto_ids: true
  footnote_nr: 1
  entity_output: as_char
  toc_levels: 1..6
  smart_quotes: lsquo,rsquo,ldquo,rdquo
  enable_coderay: false
```

### Collections Configuration
```yaml
collections:
  teaching:
    output: true
    permalink: /:collection/:path/
  publications:
    output: true
    permalink: /:collection/:path/
  portfolio:
    output: true
    permalink: /:collection/:path/
  talks:
    output: true
    permalink: /:collection/:path/
```

### Defaults (Layout and Settings per Collection)
```yaml
defaults:
  # _publications
  - scope:
      path: ""
      type: publications
    values:
      layout: single
      author_profile: true
      share: true
      comments: true
  
  # _talks
  - scope:
      path: ""
      type: talks
    values:
      layout: talk
      author_profile: true
      share: true
  
  # _teaching
  - scope:
      path: ""
      type: teaching
    values:
      layout: single
      author_profile: true
      share: true
      comments: true
  
  # _posts
  - scope:
      path: ""
      type: posts
    values:
      layout: single
      author_profile: true
      read_time: true
      comments: true
      share: true
      related: true
  
  # _pages
  - scope:
      path: ""
      type: pages
    values:
      layout: single
      author_profile: true
  
  # _portfolio
  - scope:
      path: ""
      type: portfolio
    values:
      layout: single
      author_profile: true
      share: true
```

### Sass/SCSS Configuration
```yaml
sass:
  sass_dir: _sass
  style: compressed  # compressed or expanded
```

### Outputting
```yaml
permalink: /:categories/:title/
# paginate: 5  # Amount of posts per page (uncomment to enable)
# paginate_path: /page:num/
timezone: Etc/UTC
```

### Plugins
```yaml
plugins:
  - jekyll-feed
  - jekyll-gist
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-redirect-from
  - jemoji

whitelist:  # GitHub Pages compatible plugins
  - jekyll-feed
  - jekyll-gist
  - jekyll-paginate
  - jekyll-sitemap
  - jekyll-redirect-from
  - jemoji
```

### Archives Configuration
```yaml
category_archive:
  type: liquid
  path: /categories/

tag_archive:
  type: liquid
  path: /tags/
```

### HTML Compression
```yaml
compress_html:
  clippings: all
  ignore:
    envs: development
```

---

## 5. _DATA/NAVIGATION.YML STRUCTURE

### Location: `_data/navigation.yml`

```yaml
# The following is the order of the links in the header of the website.
# Changing the order here will adjust the order and you can also add 
# additional links. Removing a link prevents it from showing in the header, 
# but does not prevent it from being included in the site.
#
# NOTE that only one of the CV options should be selected, the first is 
# for the Markdown formatted page while the second is generated using JSON.

main:
  - title: "Publications"
    url: /publications/

  - title: "Talks"
    url: /talks/    

  - title: "Teaching"
    url: /teaching/    
    
  - title: "Portfolio"
    url: /portfolio/
        
  - title: "Blog Posts"
    url: /year-archive/
    
  - title: "CV"
    url: /cv/
  
  # Alternative: CV as JSON/API
  # - title: "CV"
  #   url: /cv-json/
    
  - title: "Guide"
    url: /markdown/
```

**Structure:**
- `main:` — Primary navigation menu array
- Each item has:
  - `title:` — Text displayed in navigation
  - `url:` — Internal or external URL path

---

## 6. ESSENTIAL CONFIGURATION FILES

### GEMFILE
**Location:** `Gemfile`

Specifies Ruby gem dependencies for Jekyll and plugins:
```ruby
source "https://rubygems.org"

gem "jekyll", "~> 3.5"
gem "minimal-mistakes-jekyll"
gem "jekyll-feed"
gem "jekyll-gist"
gem "jekyll-paginate"
gem "jekyll-sitemap"
gem "jekyll-redirect-from"
gem "jemoji"
```

### PACKAGE.JSON
**Location:** `package.json`

Node.js dependencies for asset compilation and build tools.

### DOCKER CONFIGURATION
**File:** `Dockerfile` / `docker-compose.yaml`

Enables running the site in Docker containers for development/deployment without local dependencies.

### GITHUB ACTIONS WORKFLOWS
**Location:** `.github/workflows/pages-build-deployment.yml`

Automated workflow for building and deploying to GitHub Pages.

### DEVELOPMENT CONTAINER
**Location:** `.devcontainer/devcontainer.json`

VS Code Dev Container configuration for standardized development environment.

---

## 7. QUICK REFERENCE: FILE NAMING CONVENTIONS

### Publications
**Format:** `YYYY-MM-DD-publication-key.md`
```
_publications/2009-10-01-paper-title-number-1.md
_publications/2015-10-01-paper-title-number-3.md
```

### Talks
**Format:** `YYYY-MM-DD-talk-key.md`
```
_talks/2012-03-01-talk-1.md
_talks/2013-10-15-talk-2.md
```

### Teaching
**Format:** `YYYY-semester-teaching-key.md`
```
_teaching/2014-spring-teaching-1.md
_teaching/2015-fall-teaching-2.md
```

### Blog Posts
**Format:** `YYYY-MM-DD-post-slug.md`
```
_posts/2024-01-01-new-year-post.md
_posts/2024-02-14-valentine-post.md
```

### Pages
**Format:** `page-slug.md` (no date prefix)
```
_pages/about.md
_pages/cv.md
_pages/publications.html
```

---

## 8. DIRECTORY TREE OVERVIEW

```
academicpages.github.io/
├── _config.yml
├── _config_docker.yml
├── Gemfile
├── Gemfile.lock
├── package.json
├── docker-compose.yaml
├── Dockerfile
├── README.md
├── LICENSE
├── CNAME
├── .gitignore
├── .devcontainer/
│   └── devcontainer.json
├── .github/
│   └── workflows/
│       └── pages-build-deployment.yml
├── _data/
│   └── navigation.yml
├── _pages/
│   ├── 404.md
│   ├── about.md
│   ├── cv.md
│   ├── cv-json.md
│   ├── publications.html
│   ├── talks.html
│   ├── teaching.html
│   ├── portfolio.html
│   ├── year-archive.html
│   └── [other pages]
├── _layouts/
│   ├── default.html
│   ├── single.html
│   ├── talk.html
│   ├── archive.html
│   ├── cv-layout.html
│   └── [other layouts]
├── _includes/
│   ├── head.html
│   ├── masthead.html
│   ├── footer.html
│   ├── author-profile.html
│   ├── social-share.html
│   ├── archive-single.html
│   └── [50+ component files]
├── _sass/
│   └── minimal-mistakes/
│       ├── _variables.scss
│       ├── _base.scss
│       ├── _layout.scss
│       └── [other SCSS files]
├── _publications/
│   ├── 2009-10-01-paper-title-number-1.md
│   ├── 2010-10-01-paper-title-number-2.md
│   └── [other publications]
├── _talks/
│   ├── 2012-03-01-talk-1.md
│   ├── 2012-04-01-talk-2.md
│   └── [other talks]
├── _teaching/
│   ├── 2014-spring-teaching-1.md
│   ├── 2015-spring-teaching-2.md
│   └── [other teaching]
├── _posts/
│   └── [blog posts]
├── _portfolio/
│   └── [portfolio items]
├── _drafts/
│   └── [draft posts]
├── assets/
│   ├── css/
│   ├── js/
│   ├── images/
│   └── vendor/
├── files/
│   ├── slides1.pdf
│   ├── paper1.pdf
│   ├── bibtex1.bib
│   └── [downloadable files]
├── images/
│   ├── profile.png
│   ├── themes/
│   └── [theme images]
├── scripts/
│   ├── csv_to_json.py
│   ├── json_to_md.py
│   └── [utility scripts]
├── markdown_generator/
│   ├── PubsFromBib.ipynb
│   ├── PubsFromCSV.ipynb
│   └── [generator notebooks]
└── talkmap/
    ├── talkmap.py
    ├── talkmap.ipynb
    └── [talkmap files]
```

---

## 9. THEME CUSTOMIZATION POINTS

### Colors and Styling
- Edit `_sass/minimal-mistakes/_variables.scss` for color scheme
- Available themes: default, air, sunrise, mint, dirt, contrast (set in `_config.yml`)

### Navigation Menu
- Edit `_data/navigation.yml` to modify top navigation links

### Author Profile
- Edit `author:` section in `_config.yml` for sidebar information
- Edit `_includes/author-profile.html` for profile widget layout

### Footer
- Edit `_includes/footer.html` for footer content and links

### Home Page
- Edit `_pages/about.md` for home page content

### Layouts and Components
- Modify `_layouts/*.html` for page structure changes
- Modify `_includes/*.html` for component-level changes

---

## 10. DEPLOYMENT AND BUILD COMMANDS

### Local Development
```bash
# Install dependencies
bundle install

# Serve locally with live reload
jekyll serve -l -H localhost
# or
bundle exec jekyll serve -l -H localhost
```

### Docker Development
```bash
# Build and run in Docker
docker compose up
# Access at http://localhost:4000
```

### GitHub Pages Automatic Deployment
- Push to `master` branch
- GitHub Actions automatically builds and deploys to `gh-pages` branch

### Build Output
- Generated static site: `_site/` directory
- Do NOT commit `_site/` to repository (handled by GitHub Actions)

---

## 11. QUICK START CHECKLIST

- [ ] Edit `_config.yml` with your site name, URL, and author info
- [ ] Update `_data/navigation.yml` with your menu items
- [ ] Create/edit `_pages/about.md` for home page
- [ ] Create/edit `_pages/cv.md` for CV page
- [ ] Add publications to `_publications/`
- [ ] Add talks to `_talks/`
- [ ] Add teaching experience to `_teaching/`
- [ ] Add blog posts to `_posts/`
- [ ] Update social media links in `_config.yml`
- [ ] Add profile image as `assets/images/profile.png`
- [ ] Upload PDFs and files to `files/` directory
- [ ] Test locally with `jekyll serve`
- [ ] Push to GitHub repository to deploy

---

## 12. USEFUL RESOURCES

- **Official Site:** https://academicpages.github.io/
- **GitHub Repository:** https://github.com/academicpages/academicpages.github.io
- **Jekyll Documentation:** https://jekyllrb.com/
- **Markdown Guide:** https://academicpages.github.io/markdown/
- **Tutorial:** https://jayrobwilliams.com/posts/2020/06/academic-website/

