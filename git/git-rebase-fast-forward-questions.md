<div dir="rtl" align="right">

<style>
  .git-ui {
    font-family: system-ui, -apple-system, "Segoe UI", Tahoma, sans-serif;
    color: #1a1a2e;
    line-height: 1.7;
    max-width: 820px;
    margin: 0 auto;
  }
  .git-ui * { box-sizing: border-box; }
  .git-ui h1 {
    font-size: 1.75rem;
    font-weight: 800;
    margin: 0 0 0.35rem;
    color: #1a1a2e;
    letter-spacing: -0.02em;
  }
  .git-ui .subtitle {
    color: #5c5c7a;
    font-size: 0.95rem;
    margin: 0 0 1.5rem;
  }
  .git-ui .badge-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1.75rem;
  }
  .git-ui .badge {
    display: inline-block;
    padding: 0.25rem 0.65rem;
    border-radius: 999px;
    font-size: 0.78rem;
    font-weight: 600;
    background: #f0f0f5;
    color: #444466;
  }
  .git-ui .badge--accent { background: #fff0eb; color: #c44e1a; }
  .git-ui .callout {
    background: #fff5f5;
    border-right: 4px solid #ec6530;
    border-radius: 0 10px 10px 0;
    padding: 1rem 1.15rem;
    margin-bottom: 1.75rem;
  }
  .git-ui .callout-title {
    font-weight: 700;
    color: #c44e1a;
    margin-bottom: 0.5rem;
    font-size: 0.9rem;
  }
  .git-ui .callout ul {
    margin: 0;
    padding-right: 1.1rem;
    color: #3d3d55;
    font-size: 0.92rem;
  }
  .git-ui .callout li { margin-bottom: 0.3rem; }
  .git-ui .section-title {
    font-size: 1.05rem;
    font-weight: 700;
    margin: 2rem 0 0.85rem;
    padding-bottom: 0.4rem;
    border-bottom: 2px solid #ececf2;
    color: #1a1a2e;
  }
  .git-ui table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
    margin-bottom: 0.5rem;
  }
  .git-ui th {
    background: #1a1a2e;
    color: #fff;
    padding: 0.6rem 0.75rem;
    text-align: right;
    font-weight: 600;
  }
  .git-ui th:first-child { border-radius: 0 8px 0 0; }
  .git-ui th:last-child { border-radius: 8px 0 0 0; }
  .git-ui td {
    padding: 0.55rem 0.75rem;
    border-bottom: 1px solid #ececf2;
    vertical-align: top;
  }
  .git-ui tr:nth-child(even) td { background: #fafafc; }
  .git-ui .tag {
    display: inline-block;
    padding: 0.1rem 0.45rem;
    border-radius: 4px;
    font-size: 0.75rem;
    font-weight: 600;
  }
  .git-ui .tag--yes { background: #e6f7ee; color: #1a7a45; }
  .git-ui .tag--no { background: #f0f0f5; color: #666680; }
  .git-ui .tag--rewrite { background: #fff3e0; color: #b35c00; }
  .git-ui .rule-box {
    background: #f7f8fc;
    border: 1px solid #e2e4ef;
    border-radius: 10px;
    padding: 1rem 1.15rem;
    font-size: 0.9rem;
    margin-bottom: 0.5rem;
  }
  .git-ui .rule-box p { margin: 0.35rem 0; }
  .git-ui .rule-box strong { color: #1a1a2e; }
  .git-ui .cmd-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }
  @media (max-width: 560px) {
    .git-ui .cmd-grid { grid-template-columns: 1fr; }
  }
  .git-ui .cmd-card {
    background: #1a1a2e;
    color: #e8e8f0;
    border-radius: 8px;
    padding: 0.55rem 0.75rem;
    font-family: "Cascadia Code", "Fira Code", Consolas, monospace;
    font-size: 0.8rem;
    direction: ltr;
    text-align: left;
  }
  .git-ui .toc {
    background: #fafafc;
    border: 1px solid #e2e4ef;
    border-radius: 10px;
    padding: 1rem 1.15rem;
    margin-bottom: 2rem;
  }
  .git-ui .toc-title {
    font-weight: 700;
    font-size: 0.88rem;
    margin-bottom: 0.6rem;
    color: #1a1a2e;
  }
  .git-ui .toc ol {
    margin: 0;
    padding-right: 1.2rem;
    columns: 2;
    column-gap: 1.5rem;
    font-size: 0.82rem;
  }
  @media (max-width: 560px) {
    .git-ui .toc ol { columns: 1; }
  }
  .git-ui .toc a {
    color: #3b5bdb;
    text-decoration: none;
  }
  .git-ui .toc a:hover { text-decoration: underline; }
  .git-ui .qa-card {
    border: 1px solid #e2e4ef;
    border-radius: 12px;
    margin-bottom: 1.25rem;
    overflow: hidden;
  }
  .git-ui .qa-header {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
    padding: 1rem 1.15rem;
    background: #fafafc;
    border-bottom: 1px solid #e2e4ef;
  }
  .git-ui .qa-num {
    flex-shrink: 0;
    width: 2rem;
    height: 2rem;
    border-radius: 8px;
    background: #1a1a2e;
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.85rem;
  }
  .git-ui .qa-scenario {
    font-size: 0.92rem;
    color: #2d2d44;
  }
  .git-ui .qa-scenario strong {
    display: block;
    font-size: 0.78rem;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #8888a0;
    margin-bottom: 0.25rem;
    font-weight: 600;
  }
  .git-ui .qa-body {
    padding: 1rem 1.15rem;
  }
  .git-ui .qa-answer-label {
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #1a7a45;
    background: #e6f7ee;
    padding: 0.15rem 0.5rem;
    border-radius: 4px;
    margin-bottom: 0.6rem;
  }
  .git-ui .qa-body p {
    margin: 0.4rem 0;
    font-size: 0.92rem;
    color: #2d2d44;
  }
  .git-ui .qa-body blockquote {
    margin: 0.6rem 0;
    padding: 0.5rem 0.85rem;
    border-right: 3px solid #ec6530;
    background: #fff8f5;
    color: #5c3d2e;
    font-size: 0.88rem;
    border-radius: 0 6px 6px 0;
  }
  .git-ui pre {
    background: #1a1a2e !important;
    color: #e8e8f0 !important;
    border-radius: 8px;
    padding: 0.75rem 1rem !important;
    font-size: 0.82rem;
    direction: ltr;
    text-align: left;
    overflow-x: auto;
    margin: 0.6rem 0;
  }
  .git-ui code {
    font-family: "Cascadia Code", "Fira Code", Consolas, monospace;
    font-size: 0.85em;
  }
  .git-ui p code, .git-ui li code {
    background: #f0f0f5;
    padding: 0.1rem 0.35rem;
    border-radius: 4px;
    color: #c44e1a;
  }
  .git-ui hr {
    border: none;
    border-top: 1px solid #ececf2;
    margin: 2rem 0;
  }
</style>

<div class="git-ui">

<h1>سؤال‌های سناریومحور Git Pull</h1>
<p class="subtitle">Fast-Forward، Merge و Rebase — با جواب کامل</p>

<div class="badge-row">
  <span class="badge badge--accent">۲۰ سناریو</span>
  <span class="badge">Pull</span>
  <span class="badge">Rebase</span>
  <span class="badge">Merge</span>
  <span class="badge">ff-only</span>
</div>

<div class="callout">
  <div class="callout-title">خلاصه سریع</div>
  <ul>
    <li><code>git pull</code> یعنی fetch + ترکیب تغییرات remote با local.</li>
    <li>اگر local فقط عقب باشد، fast-forward انجام می‌شود.</li>
    <li>اگر local و remote هر دو commit جدید داشته باشند، branchها divergent شده‌اند.</li>
    <li>در divergent branches باید بین merge و rebase انتخاب کنیم.</li>
    <li>merge تاریخچه واقعی را حفظ می‌کند ولی ممکن است history را شلوغ کند.</li>
    <li>rebase history را خطی و تمیز می‌کند ولی commitها را بازنویسی می‌کند.</li>
    <li>ff-only فقط fast-forward را قبول می‌کند و در حالت divergent خطا می‌دهد.</li>
  </ul>
</div>

<div class="section-title">جدول مقایسه‌ای</div>

<table>
  <thead>
    <tr>
      <th>مفهوم</th>
      <th>یعنی چی؟</th>
      <th>commit جدید؟</th>
      <th>بهترین کاربرد</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Fast-forward</strong></td>
      <td>فقط branch جلو می‌رود</td>
      <td><span class="tag tag--no">نه</span></td>
      <td>وقتی local فقط عقب است</td>
    </tr>
    <tr>
      <td><strong>Merge</strong></td>
      <td>دو مسیر با merge commit یکی می‌شوند</td>
      <td><span class="tag tag--yes">بله</span></td>
      <td>branch مشترک تیمی</td>
    </tr>
    <tr>
      <td><strong>Rebase</strong></td>
      <td>commitهای local روی remote دوباره چیده می‌شوند</td>
      <td><span class="tag tag--rewrite">با hash جدید</span></td>
      <td>branch شخصی / PR</td>
    </tr>
    <tr>
      <td><strong>ff-only</strong></td>
      <td>فقط fast-forward را قبول می‌کند</td>
      <td><span class="tag tag--no">نه</span></td>
      <td>جلوگیری از merge ناخواسته</td>
    </tr>
  </tbody>
</table>

<div class="section-title">قانون تصمیم‌گیری</div>

<div class="rule-box">
  <p>اگر <strong>branch شخصی</strong> است → <code>rebase</code></p>
  <p>اگر <strong>branch مشترک تیمی</strong> است → <code>merge</code></p>
  <p>اگر <strong>نمی‌خواهی Git تصمیم بگیرد</strong> → <code>ff-only</code></p>
  <p>اگر <strong>local فقط عقب است</strong> → fast-forward</p>
  <p>اگر <strong>local و remote هر دو تغییر دارند</strong> → divergent branches</p>
</div>

<div class="section-title">دستورات اصلی</div>

<div class="cmd-grid">
  <div class="cmd-card">git pull --rebase</div>
  <div class="cmd-card">git pull --no-rebase</div>
  <div class="cmd-card">git pull --ff-only</div>
  <div class="cmd-card">git fetch origin</div>
  <div class="cmd-card">git rebase origin/main</div>
  <div class="cmd-card">git merge origin/main</div>
  <div class="cmd-card">git rebase --continue</div>
  <div class="cmd-card">git rebase --abort</div>
  <div class="cmd-card">git push --force-with-lease</div>
</div>

<hr>

<div class="toc">
  <div class="toc-title">فهرست سؤالات</div>
  <ol>
    <li><a href="#q1">لوکال فقط عقب است</a></li>
    <li><a href="#q2">انتخاب بهترین update</a></li>
    <li><a href="#q3">local و remote هر دو تغییر دارند</a></li>
    <li><a href="#q4">branch شخصی برای PR</a></li>
    <li><a href="#q5">branch مشترک تیمی</a></li>
    <li><a href="#q6">فقط fast-forward مجاز</a></li>
    <li><a href="#q7">تنظیم دائمی ff-only</a></li>
    <li><a href="#q8">خطای divergent branches</a></li>
    <li><a href="#q9">push بعد از rebase reject</a></li>
    <li><a href="#q10">push امن بعد از rebase</a></li>
    <li><a href="#q11">conflict وسط rebase</a></li>
    <li><a href="#q12">لغو کامل rebase</a></li>
    <li><a href="#q13">pull همیشه با rebase</a></li>
    <li><a href="#q14">تیم history واقعی merge</a></li>
    <li><a href="#q15">نتیجه merge</a></li>
    <li><a href="#q16">نتیجه rebase</a></li>
    <li><a href="#q17">تغییر hash بعد از rebase</a></li>
    <li><a href="#q18">گرفتن remote بدون ترکیب</a></li>
    <li><a href="#q19">rebase دستی روی origin/main</a></li>
    <li><a href="#q20">توصیه اشتباه درباره rebase</a></li>
  </ol>
</div>

<!-- Q1 -->
<div class="qa-card" id="q1">
  <div class="qa-header">
    <div class="qa-num">۱</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      روی branch شخصی خودت کار می‌کنی. هنوز هیچ commit لوکالی نداده‌ای. یکی از هم‌تیمی‌ها روی remote یک commit جدید push کرده. حالا می‌خواهی branch خودت را آپدیت کنی. اگر <code>git pull</code> بزنی چه اتفاقی می‌افتد؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>اگر branch لوکال فقط از remote عقب باشد و commit جدیدی در لوکال نداشته باشی، Git معمولاً <strong>fast-forward</strong> انجام می‌دهد.</p>
    <p>یعنی commit جدیدی ساخته نمی‌شود و فقط pointer branch جلو می‌رود.</p>
<pre>قبل:

local:  A---B
remote: A---B---C

بعد:

local:  A---B---C</pre>
  </div>
</div>

<!-- Q2 -->
<div class="qa-card" id="q2">
  <div class="qa-header">
    <div class="qa-num">۲</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      وضعیت: local روی A---B و remote روی A---B---C. تو فقط از remote عقب هستی. بهترین نوع update اینجا چیست؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>بهترین حالت اینجا <strong>fast-forward</strong> است. چون local هیچ commit اضافه‌ای ندارد.</p>
<pre>git pull</pre>
    <p>یا برای سخت‌گیرانه‌تر بودن:</p>
<pre>git pull --ff-only</pre>
  </div>
</div>

<!-- Q3 -->
<div class="qa-card" id="q3">
  <div class="qa-header">
    <div class="qa-num">۳</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      local: A---B---D و remote: A---B---C. تو هم commit داری، remote هم commit جدید دارد. این وضعیت چه نامی دارد؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>این وضعیت <strong>divergent branches</strong> است — local و remote از یک نقطه مشترک جدا شده‌اند.</p>
<pre>local فقط D را دارد.
remote فقط C را دارد.</pre>
    <p>در این حالت fast-forward ممکن نیست و باید بین <strong>merge</strong> و <strong>rebase</strong> تصمیم بگیری.</p>
  </div>
</div>

<!-- Q4 -->
<div class="qa-card" id="q4">
  <div class="qa-header">
    <div class="qa-num">۴</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      روی branch شخصی برای Pull Request کار می‌کنی. می‌خواهی history تمیز و خطی بماند. remote branch اصلی هم آپدیت شده. کدام دستور مناسب‌تر است؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>برای branch شخصی، معمولاً <code>rebase</code> مناسب‌تر است:</p>
<pre>git pull --rebase</pre>
    <p>یا دقیق‌تر:</p>
<pre>git fetch origin
git rebase origin/main</pre>
    <p>چون rebase commitهای تو را روی آخرین نسخه remote می‌چیند و history خطی‌تر می‌ماند.</p>
  </div>
</div>

<!-- Q5 -->
<div class="qa-card" id="q5">
  <div class="qa-header">
    <div class="qa-num">۵</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      روی branch مشترک <code>develop</code> کار می‌کنی. branch تو و remote هر دو تغییرات جدید دارند. برای کمتر دردسر برای بقیه، merge بهتر است یا rebase؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>در branch مشترک تیمی معمولاً <strong>merge</strong> امن‌تر است.</p>
<pre>git pull --no-rebase</pre>
    <p>یا:</p>
<pre>git fetch origin
git merge origin/develop</pre>
    <p>merge تاریخچه را بازنویسی نمی‌کند؛ rebase commitها را دوباره می‌سازد و ممکن است برای بقیه مشکل ایجاد کند.</p>
  </div>
</div>

<!-- Q6 -->
<div class="qa-card" id="q6">
  <div class="qa-header">
    <div class="qa-num">۶</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      می‌خواهی Git فقط وقتی pull کند که branch تو فقط عقب‌تر از remote باشد. اگر divergent بودند، خطا بدهد. کدام دستور مناسب است؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>git pull --ff-only</pre>
    <blockquote>فقط اگر fast-forward ممکن بود pull کن؛ اگر branchها divergent بودند، خطا بده.</blockquote>
    <p>این گزینه برای جلوگیری از merge ناخواسته خیلی خوب است.</p>
  </div>
</div>

<!-- Q7 -->
<div class="qa-card" id="q7">
  <div class="qa-header">
    <div class="qa-num">۷</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      می‌خواهی برای همیشه تنظیم کنی که <code>git pull</code> فقط در حالت fast-forward مجاز باشد. کدام config را می‌زنی؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>git config --global pull.ff only</pre>
    <p>اگر branchها divergent باشند، Git خطا می‌دهد و باید آگاهانه تصمیم بگیری:</p>
<pre>git pull --rebase</pre>
    <p>یا:</p>
<pre>git pull --no-rebase</pre>
  </div>
</div>

<!-- Q8 -->
<div class="qa-card" id="q8">
  <div class="qa-header">
    <div class="qa-num">۸</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      بعد از <code>git pull</code> این خطا را می‌بینی: <code>fatal: Need to specify how to reconcile divergent branches.</code> این خطا یعنی چه؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>یعنی local و remote هر دو commitهایی دارند که طرف مقابل ندارد. Git نمی‌داند باید با <strong>merge</strong> یکی کند یا با <strong>rebase</strong>.</p>
<pre>git pull --rebase
# یا
git pull --no-rebase
# یا
git pull --ff-only</pre>
  </div>
</div>

<!-- Q9 -->
<div class="qa-card" id="q9">
  <div class="qa-header">
    <div class="qa-num">۹</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      روی branch شخصی rebase انجام داده‌ای. بعد <code>git push</code> می‌زنی و reject می‌شود. چرا؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>چون <code>rebase</code> تاریخچه را بازنویسی می‌کند. Commit قبلی مثلاً <code>D</code> بوده، بعد از rebase تبدیل شده به <code>D'</code>. hash تغییر کرده حتی اگر محتوا یکی باشد.</p>
<pre>قبل:  A---B---D
بعد:  A---B---C---D'</pre>
    <p>remote هنوز commit قدیمی را می‌شناسد؛ push معمولی reject می‌شود.</p>
  </div>
</div>

<!-- Q10 -->
<div class="qa-card" id="q10">
  <div class="qa-header">
    <div class="qa-num">۱۰</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      branch شخصی است و مطمئنی کسی دیگر روی آن کار نمی‌کند. بعد از rebase باید push کنی. کدام دستور امن‌تر از <code>git push --force</code> است؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>git push --force-with-lease</pre>
    <p>اگر کسی قبل از تو روی remote push کرده باشد، Git اجازه overwrite نمی‌دهد.</p>
  </div>
</div>

<!-- Q11 -->
<div class="qa-card" id="q11">
  <div class="qa-header">
    <div class="qa-num">۱۱</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      وسط rebase conflict پیش آمده. conflictها را حل کرده‌ای. بعد از حل conflict چه دو دستور اصلی بزنی؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>git add .
git rebase --continue</pre>
  </div>
</div>

<!-- Q12 -->
<div class="qa-card" id="q12">
  <div class="qa-header">
    <div class="qa-num">۱۲</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      وسط rebase conflict پیش آمده ولی می‌خواهی کل rebase را لغو کنی. کدام دستور؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>git rebase --abort</pre>
    <p>branch را به وضعیت قبل از شروع rebase برمی‌گرداند.</p>
  </div>
</div>

<!-- Q13 -->
<div class="qa-card" id="q13">
  <div class="qa-header">
    <div class="qa-num">۱۳</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      می‌خواهی هر بار <code>git pull</code> به جای merge، rebase انجام شود. کدام config؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>git config --global pull.rebase true</pre>
    <p>بعد از این، <code>git pull</code> مثل <code>git pull --rebase</code> رفتار می‌کند.</p>
  </div>
</div>

<!-- Q14 -->
<div class="qa-card" id="q14">
  <div class="qa-header">
    <div class="qa-num">۱۴</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      تیم history واقعی mergeها را می‌خواهد و نمی‌خواهد commitها بازنویسی شوند. تنظیم پیش‌فرض <code>git pull</code> چیست؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>git config --global pull.rebase false</pre>
    <p>یعنی pull به صورت پیش‌فرض merge انجام می‌دهد — برای branch مشترک تیمی امن‌تر است.</p>
  </div>
</div>

<!-- Q15 -->
<div class="qa-card" id="q15">
  <div class="qa-header">
    <div class="qa-num">۱۵</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      وضعیت: A---B---D و \---C. بعد از merge چه چیزی به history اضافه می‌شود؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>یک <strong>merge commit</strong> جدید ساخته می‌شود:</p>
<pre>A---B---D---M
     \---C---/</pre>
    <p>Commit <code>M</code> نشان می‌دهد دو مسیر جداشده دوباره ترکیب شده‌اند.</p>
  </div>
</div>

<!-- Q16 -->
<div class="qa-card" id="q16">
  <div class="qa-header">
    <div class="qa-num">۱۶</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      local: A---B---D و remote: A---B---C. بعد از rebase، history تقریباً به چه شکلی می‌شود؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>A---B---C---D'</pre>
    <p>Commit <code>D</code> به <code>D'</code> تبدیل می‌شود چون Git آن را دوباره ساخته است.</p>
  </div>
</div>

<!-- Q17 -->
<div class="qa-card" id="q17">
  <div class="qa-header">
    <div class="qa-num">۱۷</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      بعد از rebase commit قبلی hash جدید دارد. آیا طبیعی است؟ چرا؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>بله، طبیعی است. rebase commitها را روی base جدید می‌سازد؛ وقتی parent تغییر کند، hash هم تغییر می‌کند.</p>
  </div>
</div>

<!-- Q18 -->
<div class="qa-card" id="q18">
  <div class="qa-header">
    <div class="qa-num">۱۸</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      می‌خواهی فقط آخرین تغییرات remote را بگیری، بدون ترکیب با branch فعلی. کدام دستور؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>git fetch origin</pre>
    <p><code>fetch</code> تغییرات را می‌گیرد ولی merge/rebase نمی‌کند. بعد تصمیم بگیر:</p>
<pre>git rebase origin/main
# یا
git merge origin/main</pre>
  </div>
</div>

<!-- Q19 -->
<div class="qa-card" id="q19">
  <div class="qa-header">
    <div class="qa-num">۱۹</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      روی <code>feature/login</code> هستی و می‌خواهی آن را روی آخرین <code>origin/main</code> بنشانی، بدون pull مستقیم.
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
<pre>git fetch origin
git rebase origin/main</pre>
  </div>
</div>

<!-- Q20 -->
<div class="qa-card" id="q20">
  <div class="qa-header">
    <div class="qa-num">۲۰</div>
    <div class="qa-scenario">
      <strong>سناریو</strong>
      هم‌تیمی می‌گوید: «برای history تمیز، همیشه روی branch مشترک تیمی rebase بزن.» آیا این توصیه همیشه درست است؟
    </div>
  </div>
  <div class="qa-body">
    <div class="qa-answer-label">جواب</div>
    <p>نه. <code>rebase</code> history را بازنویسی می‌کند و روی branch مشترک می‌تواند commitهای افراد را ناسازگار کند.</p>
    <p>branch شخصی → <code>git pull --rebase</code> معمولاً خوب است.</p>
    <p>branch مشترک → <code>git pull --no-rebase</code> معمولاً امن‌تر است.</p>
    <div class="rule-box" style="margin-top: 0.75rem;">
      <p><strong>branch شخصی</strong> → rebase</p>
      <p><strong>branch مشترک</strong> → merge</p>
      <p><strong>احتیاط کامل</strong> → ff-only</p>
    </div>
  </div>
</div>

</div>
</div>
