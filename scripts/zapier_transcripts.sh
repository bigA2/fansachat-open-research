# Transcripts (auto subtitles) of Zapier's own YouTube tutorials on building Zaps and handling errors. No AI.
set +e
mkdir -p results/zapier/transcripts
for q in "Zapier autoreplay" "Zapier troubleshoot zap errors" "Zapier Copilot build zap" "Zapier zap history errors" "Zapier how to build your first zap"; do
  yt-dlp "ytsearch3:$q" --skip-download --write-auto-subs --sub-langs en --sub-format vtt --print "%(id)s|%(channel)s|%(title)s|%(duration)s" \
    -o "results/zapier/transcripts/%(id)s.%(ext)s" >> results/zapier/transcripts/index.txt 2>> results/zapier/transcripts/errors.txt
done
# vtt -> plain text (drop timing lines and repeats)
for f in results/zapier/transcripts/*.vtt; do [ -e "$f" ] || continue
  grep -v -e '-->' -e '^WEBVTT' -e '^Kind:' -e '^Language:' -e '^$' "$f" | sed 's/<[^>]*>//g' | awk '!seen[$0]++' > "${f%.vtt}.txt"; rm "$f"; done
ls results/zapier/transcripts | head -40
