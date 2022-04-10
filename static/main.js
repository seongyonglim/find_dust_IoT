Kakao.init('5d91c3f6976877c89f9b267b24d8db6f');

var login_btns = [];

login_btns.push(document.getElementsByClassName("btn__profile"));

console.log(login_btns);

var is_login = false;

var login_txt = "로그인";

var user_id;

login_btns.forEach(element => element[0].textContent = login_txt);

function login()
{
    is_login==false?kakaoLogin():kakaoLogout();
}

//카카오 로그인
function kakaoLogin() {
    Kakao.Auth.login({
        success: function (response) {
            Kakao.API.request({
                url: '/v2/user/me',
                success: function (response) {
                    is_login=true;
                    login_txt = is_login?"로그아웃":"로그인";
                    login_btns.forEach(element => element[0].textContent = login_txt);
                    user_id=response;
                    $.get(
                        "/login?id="+user_id.id,
                        function(response) {
                            console.log(response);
                        }
                     )
                },
                fail: function (error) {
                    console.log(error)
                },
            })
        },
        fail: function (error) {
            console.log(error)
        },
    })
}
//카카오 로그아웃  
function kakaoLogout() {
    if (Kakao.Auth.getAccessToken()) {
        Kakao.API.request({
            url: '/v1/user/unlink',
            success: function (response) {
                //console.log(response)
                is_login=false;
                login_txt = is_login?"로그아웃":"로그인";
            
                login_btns.forEach(element => element[0].textContent = login_txt);
            },
            fail: function (error) {
                console.log(error)
            },
        })
        Kakao.Auth.setAccessToken(undefined)
    }
} 

const tabs = document.querySelector(".tabs");
const tabsLi = tabs.querySelectorAll(".tabs__li");
const tabsContents = tabs.querySelectorAll(".tabs__content");

function displayCurrentTab(current) {
  for (let i = 0; i < tabsContents.length; i++) {
    tabsContents[i].style.display = (current === i) ? "block" : "none";
  }
}
displayCurrentTab(0);

tabs.addEventListener("click", event => {
  if (event.target.className === "tabs__li") {
    for (let i = 0; i < tabsLi.length; i++) {
      if (event.target === tabsLi[i]) {
        displayCurrentTab(i);
        break;
      }
    }
  }
});
