---
name: flexxable-invoice
description: Draft the monthly Flexxable invoice in Canva. Use when Joey says "invoice Flexxable", "monthly invoice", "flexxable invoice", "/flexxable-invoice", or asks to send out last month's invoice. Duplicates the Canva template, fills in the new invoice number/dates/commission lines, pulls a live XE exchange rate, recalculates the totals, and leaves it as an unsent Canva draft for Joey to check before sending.
---

# /flexxable-invoice — draft the monthly Flexxable invoice

Builds the invoice as a Canva draft only. **Never sends, exports, or emails
it** — that's Joey's call, and export/send is a separate explicit ask even
after the draft looks right.

Source of truth for invoice history and the next invoice number:
`clients/flexxable/invoices.md`. Always read it first — never guess the
next `INV-XX` number.

Master Canva template: `DAEpgkPBu9c`
(https://www.canva.com/design/DAEpgkPBu9c/8Dm2SjWQjout895tn7o89w/edit).
Its saved state reflects however the last invoice was left, so always
duplicate it fresh rather than editing it directly.

## The run

### 1. Confirm the period
Default: the calendar month that just ended (e.g. run on/after 1 Sep →
period = August). If ambiguous, ask Joey rather than guess.

### 2. Get the next invoice number
Read `clients/flexxable/invoices.md`, take the last logged invoice, +1.

### 3. Ask for this period's ROYA commission sales
Don't guess or carry over a prior month's names. Ask Joey: "any ROYA sales
to add commission for this period, and at what amount each?" Default is
$300/sale unless he says otherwise. If none, the invoice is retainer-only
(matches most months per Joey).

### 4. Compute the USD total
$10,000 retainer + (commission amount × number of named sales).

### 5. Get the live exchange rate
Open `https://www.xe.com/en-us/currencyconverter/convert/?Amount=<TOTAL_USD>&From=USD&To=GBP`
in the browser tool and read the mid-market rate off the page (the
"1 USD = X GBP" line — this is the same number Joey reads when he googles
it and clicks through to XE). Multiply by the USD total for Total (GBP),
round to 2dp. Then, from that **rounded** GBP total (not the raw product —
this matches how past invoices were computed):
- VAT 20% (GBP) = round(Total GBP × 0.2, 2)
- Total Payable (GBP) = round(Total GBP × 1.2, 2)

### 6. Duplicate the template
`copy-design` on `DAEpgkPBu9c` (all pages). This is the draft — don't touch
the master.

### 7. Edit page 1
Open an editing transaction (`read-design` with `open_transaction: true`,
`page_indices: [1]`) to get current locator_ids — they can shift between
copies, don't reuse ones from a past run. Replace:
- **Invoice: INV-XX** → the new number
- **Issued: Xth MON YYYY** → today, ordinal day + month abbreviation in caps
  (e.g. "Issued: 1st SEP 2026")
- **Due date: Xth mon yyyy** → issued date + 5 calendar days, month
  abbreviation lowercase (e.g. "Due date: 6th sep 2026") — matches the
  template's existing casing split between the two fields, don't "fix" it
- The items name column: "Monthly Retainer" plus one line per named ROYA
  sale (omit entirely if none this period)
- The items amount column: "$10,000.00" plus one "$XXX.00" line per sale,
  same order as the names
- **Total (USD)**, **Total (GBP)**, **VAT 20% (GBP)**, **Total Payable
  (GBP)** — the four figures from step 5

Ordinal suffix rule: 1st/21st/31st, 2nd/22nd, 3rd/23rd, everything else
(including 11th–13th) "th".

### 8. Verify before committing
Compare the before/after thumbnails the tool returns and check the
`document` payload for the actual new text — this is a financial document,
don't skip the check. Fix anything wrong, then `finalize: "commit"`.

### 9. Log it
Add a row to `clients/flexxable/invoices.md`: invoice number, period,
issued/due dates, commission names + total, USD total, the XE rate used,
GBP total, VAT, total payable, and the Canva draft URL — mark it
**DRAFT, not yet sent**.

### 10. Hand back
Give Joey the Canva edit URL and a one-line summary of the totals. Stop
there — sending/exporting the invoice is a separate step he asks for
explicitly.

Related: [[Flexxable]]
