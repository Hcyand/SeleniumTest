html = """
<div class="hhh">
    <div class="ddd">
        <h1>1</h1>
    </div>
    <div>
        <li>4</li>
    </div>
    <ul class="eee sss">
        <li>
            <div>
                <a href="111">5</a>
            </div>
        </li>
        <li>3</li>
    </ul>
</div>
"""

from pyquery import PyQuery as pq
doc = pq(html)
lis = doc('#hhh .eee.sss li').items()
print(type(lis))
for li in lis:
    print(li)