//支持ES6用自带拷贝
async function navigatorCopy(text) {
    await navigator.clipboard.writeText(text);
}

//老式生成textarea执行拷贝指令
function textareaCopy(text) {
    let textarea = document.createElement("textarea");

    textarea.style.fontSize = "12pt";
    // Reset box model
    textarea.style.border = "0";
    textarea.style.padding = "0";
    textarea.style.margin = "0";
    // Move element out of screen horizontally
    textarea.style.position = "absolute";
    textarea.style.left = "-9999px";
    // Move element to the same position vertically
    let yPosition = window.pageYOffset || document.documentElement.scrollTop;
    textarea.style.top = yPosition + "px";

    document.body.appendChild(textarea);

    textarea.value = text;
    textarea.setAttribute("readonly", "");

    textarea.focus();
    textarea.select();
    textarea.setSelectionRange(0, textarea.value.length);

    document.execCommand("copy");
    textarea.remove();
}

//给目标营造选中效果
function targetSelection(target) {
    if (window.getSelection) {
        let selection = window.getSelection(),
            range = document.createRange();
        range.selectNodeContents(target);
        selection.removeAllRanges();
        selection.addRange(range);
    }
}

//点击操作
document.addEventListener("click", async function (e) {
    let target = e.target;
    //点击中英文选中并拷贝内容
    if (target.classList.contains("name") || target.tagName === "CODE") {
        let optid = document.querySelector("#optid");
        let text = optid.checked ? target.innerText : `give @a ${target.innerText} `;
        navigator.clipboard ? navigatorCopy(text) : textareaCopy(text);
        targetSelection(target); //选中不是必须的，就是屏幕上显示舒服点
    }
    //点击游戏规则生成规则指令
    if (target.classList.contains("rule-value")) {
        let ruleValue = target.innerText,
            ruleCmd = target.parentElement.querySelector(".rule-cmd").innerText,
            ruleText = `gamerule ${ruleCmd} ${ruleValue}`;
        navigator.clipboard ? navigatorCopy(ruleText) : textareaCopy(ruleText);
        targetSelection(target);
    }
    if (target.classList.contains("enchant-text")) {
        let enchantText = target.getAttribute("data-enchant");
        navigator.clipboard ? navigatorCopy(enchantText) : textareaCopy(enchantText);
    }
    
    //点击图标打开wiki
    if (
        target.classList.contains("sprite-block") ||
        target.classList.contains("sprite-stuff") ||
        target.classList.contains("sprite-entity")
    ) {
        let wikiBase = "https://minecraft.fandom.com/zh/wiki/";
        // let wikiBase = "https://wiki.biligame.com/mc/"; //国内镜象
        window.open(`${wikiBase}${target.parentElement.querySelector(".name").innerText}`, "wiki");
    }
});

//过滤器
let items = Array.from(document.querySelectorAll(".item")),
    titles = Array.from(document.querySelectorAll(".title")),
    filterInput = document.querySelector("#optfilter"),
    optList = items.map((i) => [i, i.innerText]),
    optJump = document.querySelector("#optjump");

if (filterInput) {
    filterInput.addEventListener("keyup", function () {
        let reg = new RegExp(filterInput.value);
        titles.forEach((item) => {
            item.style.display = filterInput.value === "" ? "block" : "none";
        });
        optList.forEach((item) => {
            item[0].style.display = item[1].match(reg) ? "inline-block" : "none";
        });
    });
}

//生成锚点跳转器
if (optJump) {
    titles.forEach((item) => {
        let text = item.querySelector("a").attributes["name"].textContent,
            opt = document.createElement("option");
        opt.value = text;
        opt.innerText = text;
        optJump.appendChild(opt);
    });
    optJump.addEventListener("change", function (e) {
        location.replace("#" + optJump.options[optJump.selectedIndex].value);
    });
}

//通过锚点生成可视title
titles.forEach((item) => {
    item.innerHTML += item.querySelector("a").attributes["name"].textContent;
});
