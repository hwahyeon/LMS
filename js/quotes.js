const quotes = [
    {
        quote: "길을 모르고 여기저기 찍힌 수많은 사랑의 발자국을 좇아 다니기에 바빴던 너희들의 어설픈 사랑을 그대로 담으려 했다.",
        refer: "이묘신",
    },
    {
        quote: "너는 1등 하지 마 / 그 자리 놓칠까 봐 늘 불안해 / 가슴에 찰싹 붙은 그 말 / 영석인 지금 뭘 할까?",
        refer: "「너는 1등 하지 마」 중에서",
    },
    {
        quote: "벽시계와 똑같이 / 시간을 보내며 / 어둠 속에서도 놀지 않고 / 제 할 일 다하며 산 / 내 손목시계!",
        refer: "「찾았다」 중에서",
    },
    {
        quote: "나무에 앉았던 새가 / 똑! / 똑! / 똑! / 떨어뜨리고 간 똥이 / 예쁜 꽃으로 피어 있었다",
        refer: "「너도 꽃」 중에서",
    }
];

const quote = document.querySelector("#quote span:first-child");
const refer = document.querySelector("#quote span:last-child");

const todaysQuote = quotes[Math.floor(Math.random() * quotes.length)];

quote.innerText = todaysQuote.quote;
refer.innerText = todaysQuote.refer;