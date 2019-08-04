export function addEntrySummary(slug, title, date, summary) {
  return {
    type: 'ADD_ENTRY_SUMMARY',
    slug,
    title,
    date,
    summary,
  };
}
