# O*NET recency check (1 Nov 2026)

## Answer

- **Release we used:** O*NET **31.0** (`results/teams.json` -> `"onet_version": "31_0"`). The script
  `scripts/build_teams.py` downloads `https://www.onetcenter.org/dl_files/database/db_31_0_text.zip`.
- **Newest release listed on onetcenter.org:** **31.0, August 2026**. The archive page says: "The current production
  release of the O*NET database is 31.0" and lists "O*NET 31.0 August 2026" at the top, above 30.3 (May 2026),
  30.2 (February 2026), 30.1 (December 2025) and 30.0 (August 2025).
  Source: https://www.onetcenter.org/db_releases.html (crawled copy: `results/sources/onet/01.md`).
- **Is it current for October 2026?** **Yes.** We use the newest production release. No newer release was listed
  when the page was crawled.
- **Newer data we could not download?** **None found.** The script got 31.0, which is the newest listed release.

## Why the next release is not out yet

The database page says O*NET "currently makes updates to the O*NET Database on a quarterly basis, with a primary
update occurring in the 3rd quarter of each year". Source: https://www.onetcenter.org/database.html
(`results/sources/onet/00.md`). Looking at past releases (Aug 2025 -> Dec 2025 -> Feb 2026 -> May 2026 -> Aug 2026),
a 31.1 release may come around the end of 2026. This is a guess from the pattern, not a stated date. I could not open
the publication schedule (https://www.onetcenter.org/ombclearance.html#schedule): **source not reached** (the host is
blocked by this session's network policy).

## What changed in 31.0 that matters to us

- 31.0 updates 208 occupations, including task statement ratings for 205 occupations and job titles for 208
  (https://www.onetcenter.org/database.html).
- The software file is now called **Software Skills** (it was "Technology Skills"). The database page lists
  "Software Skills" with documentation at https://www.onetcenter.org/dictionary/31.0/excel/software_skills.html.
  Our script already handles both names (commit `7c12b5f`).

## Action

Re-run the scripts when 31.1 (or later) appears on https://www.onetcenter.org/db_releases.html. Nothing to do now.

Data credit: O*NET 31.0 Database, USDOL/ETA, CC BY 4.0.
