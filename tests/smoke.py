"""Browser validation; requires Playwright and Chromium. Run after build.py.

Start python3 -m http.server 8765 --bind 127.0.0.1 in the repo, then run this.
No external requests are needed by the app.
"""
from collections import Counter
from pathlib import Path
from playwright.sync_api import sync_playwright

URL='http://127.0.0.1:8765/dist/study-tool.html'
errors=[]
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    ctx=browser.new_context(viewport={'width':1440,'height':1000})
    page=ctx.new_page()
    page.on('pageerror',lambda e: errors.append(str(e)))
    page.goto(URL)
    data=page.evaluate('window.STUDY_DATA')
    questions={q['prompt']:q for q in data['questions']}
    assert len(questions)==82
    assert page.locator('.topic-card').count()==6
    page.screenshot(path='/tmp/inference-desktop.png',full_page=True)
    page.locator('[data-mode="learn"]').click()
    total_lessons=0
    for topic in data['topics']:
        page.locator('[data-topic="'+topic['id']+'"]').click()
        assert page.locator('h2').inner_text()==topic['title']
        assert page.locator('.lesson').count()==len(topic['sections'])
        total_lessons+=page.locator('.lesson').count()
    assert total_lessons==31
    page.locator('[data-mode="flashcards"]').click()
    page.locator('#unlearned').check()
    for i in range(30):
        assert page.locator('.flashcard-answer').count()==0
        page.locator('#reveal').click()
        assert page.locator('.flashcard-answer').inner_text()
        page.locator('#got-it').click()
    assert 'All caught up.' in page.locator('#view').inner_text()
    page.locator('[data-mode="practice"]').click()
    seen=set()
    for kind,count in [('practice',30),('original',52)]:
        page.locator('#practice-kind').select_option(kind)
        for i in range(count):
            prompt=page.locator('.question-prompt').inner_text()
            q=questions[prompt]
            assert q['kind']==kind
            assert q['id'] not in seen
            seen.add(q['id'])
            assert page.locator('.feedback').count()==0
            assert page.locator('#submit-answer').is_disabled()
            answer=(q['answer']+1)%4 if i%3==0 else q['answer']
            page.locator('input[name="practice-answer"][value="'+str(answer)+'"]').check()
            page.locator('#submit-answer').click()
            assert page.locator('.reason-list li').count()==4
            assert page.locator('.option.correct').inner_text().endswith(q['options'][q['answer']])
            assert q['explanation'] in page.locator('.feedback').inner_text()
            page.locator('.feedback summary').click()
            assert q['source'] in page.locator('.feedback').inner_text()
            page.locator('#next-question').click()
    assert len(seen)==82
    page.reload()
    assert page.locator('.stat-number').nth(0).inner_text().startswith('82')
    assert page.locator('.stat-number').nth(2).inner_text().startswith('30')
    page.locator('[data-mode="exam"]').click()
    page.locator('#begin-exam').click()
    assert page.locator('[data-jump]').count()==20
    assert page.locator('#exam-clock').inner_text().startswith(('69:','70:'))
    assert page.locator('.feedback').count()==0
    picked=[]
    for i in range(20):
        q=questions[page.locator('.question-prompt').inner_text()]
        assert q['kind']=='original'
        picked.append(q)
        if i!=1:
            answer=(q['answer']+1)%4 if i==0 else q['answer']
            page.locator('input[name="exam-answer"][value="'+str(answer)+'"]').check()
        assert page.locator('.feedback').count()==0
        if i<19:page.locator('#exam-next').click()
    assert Counter(q['topic'] for q in picked)==Counter({'sampling':3,'mean-ci':3,'proportion-ci':3,'testing':4,'two-sample':3,'chi-square':4})
    page.locator('[data-jump="0"]').click()
    assert page.locator('input[name="exam-answer"]:checked').input_value()==str((picked[0]['answer']+1)%4)
    page.on('dialog',lambda d:d.accept())
    page.locator('#finish-exam').click()
    assert page.locator('.results-score').inner_text().startswith('18')
    assert page.locator('.review-item').count()==20
    assert '1 unanswered' in page.locator('#view').inner_text()
    page.locator('#mock-missed').click()
    assert page.locator('#missed-only').is_checked()
    assert 'Question 1 of 2' in page.locator('#view').inner_text()
    page.locator('[data-mode="exam"]').click()
    page.locator('#retry-mock').click()
    page.locator('#begin-exam').click()
    page.locator('[data-mode="learn"]').click()
    page.evaluate('const realNow=Date.now;Date.now=()=>realNow()+71*60*1000')
    page.wait_for_selector('.results-score')
    assert page.locator('.results-score').inner_text().startswith('0')
    assert '20 unanswered' in page.locator('#view').inner_text()
    page.reload()
    assert 'Last mock:' in page.locator('#view').inner_text()
    page.locator('[data-mode="formulas"]').click()
    assert page.locator('.formula-card').count()==31
    page.locator('[data-mode="practice"]').click()
    page.set_viewport_size({'width':390,'height':844})
    assert page.evaluate('document.documentElement.scrollWidth<=window.innerWidth'), 'Mobile overflow'
    page.screenshot(path='/tmp/inference-mobile.png',full_page=True)
    page.locator('#reset-main').click()
    page.locator('[data-mode="dashboard"]').click()
    assert page.locator('.stat-number').nth(0).inner_text().startswith('0')
    assert page.locator('.stat-number').nth(2).inner_text().startswith('0')
    page.goto('http://127.0.0.1:8765/dist/study-guide.html')
    page.pdf(path=str(Path(__file__).resolve().parents[1]/'dist'/'study-guide.pdf'),format='A4',print_background=True)
    ctx.close()
    blocked=browser.new_context()
    blocked.add_init_script("Storage.prototype.getItem=function(){throw new Error('blocked')};Storage.prototype.setItem=function(){throw new Error('blocked')}")
    page=blocked.new_page()
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.goto(URL)
    assert 'blocking storage' in page.locator('#storage-note').inner_text()
    page.locator('[data-mode="practice"]').click()
    page.locator('input[name="practice-answer"][value="0"]').check()
    page.locator('#submit-answer').click()
    assert page.locator('.feedback').count()==1
    assert not errors, errors
    browser.close()
    print('PASS: 82 questions/feedback/source citations; 31 lessons; 30 flashcards; reload persistence; 20-question weighted original mock; answer navigation; unanswered scoring; missed review; 70-minute timer expiration while outside exam; reset; storage-blocked fallback; mobile layout; printable PDF. No browser errors.')
