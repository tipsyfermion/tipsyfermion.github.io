# My Academic Website

This is an academic personal website based on the [Academic Pages](https://academicpages.github.io) template, which is a fork of the [Minimal Mistakes Jekyll theme](https://mmistakes.github.io/minimal-mistakes/).

**Website:** [https://debbh.me](https://debbh.me)

## Quick Start Guide

### 1. Edit Configuration (`_config.yml`)

Update your personal information:
- Author name, bio, location
- Email and social media profiles (GitHub, LinkedIn, Google Scholar, ORCID, etc.)
- Website URL

### 2. Add Content

The following directories contain template files ready for your content:

- **`_pages/`** - Static pages (Publications, Talks, Teaching, Portfolio, CV, etc.)
- **`_publications/`** - Your academic publications and papers
- **`_talks/`** - Conference talks and presentations  
- **`_teaching/`** - Courses and educational materials
- **`_portfolio/`** - Projects and work samples
- **`_posts/`** - Blog posts

Sample files have been provided in each collection to show you the correct format.

### 3. Customize Your Homepage

Edit `index.md` to replace the placeholder welcome message with your own introduction.

### 4. Update Your CV

Edit `_pages/cv.md` to add your education, work experience, and skills.

### 5. Add Profile Picture

Replace `assets/images/profile.jpg` with your own profile picture.

### 6. Customize Navigation

Edit `_data/navigation.yml` to customize the top navigation menu.

## Project Structure

```
├── _config.yml           # Site configuration
├── _data/
│   └── navigation.yml    # Navigation menu
├── _pages/               # Static pages
├── _publications/        # Publications/papers
├── _talks/               # Talks and presentations
├── _teaching/            # Teaching materials
├── _portfolio/           # Portfolio items
├── _posts/               # Blog posts
├── assets/
│   └── images/           # Images and profile picture
├── files/                # Downloadable files (PDFs, etc.)
├── index.md              # Homepage
└── Gemfile               # Ruby dependencies
```

## Installation & Local Development

To run this site locally:

```bash
# Install dependencies
bundle install

# Run local server
bundle exec jekyll serve

# Visit http://localhost:4000 in your browser
```

## Deployment

This site is designed to be hosted on GitHub Pages. Simply push your changes to your GitHub repository, and the site will automatically build and deploy.

## Resources

- [Academic Pages Guide](https://academicpages.github.io/markdown/)
- [Minimal Mistakes Documentation](https://mmistakes.github.io/minimal-mistakes/docs/configuration/)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Getting Started Guide](/getting-started/)

## Customization

This theme is highly customizable. You can:
- Modify colors and styles by editing `_sass/` files
- Change layouts in `_layouts/` directory
- Add custom CSS to `assets/css/`
- Customize includes in `_includes/` directory

For more information, see the [Minimal Mistakes theme documentation](https://mmistakes.github.io/minimal-mistakes/).

## Support

For issues or questions about the Academic Pages template, visit the [GitHub repository](https://github.com/academicpages/academicpages.github.io) or check the [wiki](https://github.com/academicpages/academicpages.github.io/wiki).

---

**Created:** March 2026  
**Theme:** Academic Pages / Minimal Mistakes