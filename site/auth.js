/* Physical Revolt — passwordless sign-in widget (vanilla, no deps).
   Renders into any element with id="pr-auth-slot". Talks to same-origin /api/auth. */
(function () {
  var API = "/api/auth";

  var css = "\
#pr-auth-slot{display:inline-flex;align-items:center;gap:10px}\
#pr-auth-slot a{cursor:pointer}\
.pr-nick{font-weight:800;color:var(--teal,#0e9a89)}\
#pr-modal{position:fixed;inset:0;z-index:9999;display:none;align-items:center;justify-content:center;\
  background:rgba(30,15,5,.45)}\
#pr-modal.on{display:flex}\
.pr-card{background:var(--card,#fffdf9);color:var(--fg,#2b211a);border:1px solid var(--line,#e8dcc4);\
  border-radius:16px;padding:26px 24px;max-width:380px;width:calc(100% - 40px);\
  box-shadow:0 24px 60px rgba(120,80,20,.28);font-family:-apple-system,'Apple SD Gothic Neo','Noto Sans KR',sans-serif}\
.pr-card h3{margin:0 0 6px;font-size:22px;font-weight:900}\
.pr-card p{margin:0 0 16px;color:var(--muted,#8a7b66);font-size:14px;line-height:1.6}\
.pr-card input{width:100%;box-sizing:border-box;padding:12px 14px;border:1px solid var(--line,#e8dcc4);\
  border-radius:10px;font-size:15px;background:var(--bg,#fbf5e9);color:inherit}\
.pr-card button{margin-top:12px;width:100%;padding:12px;border:none;border-radius:10px;cursor:pointer;\
  font-weight:800;font-size:15px;background:var(--accent,#e0442e);color:#fff}\
.pr-card .pr-x{position:absolute;top:14px;right:18px;cursor:pointer;color:var(--muted,#8a7b66);font-size:20px}\
.pr-wrap{position:relative}.pr-msg{margin-top:12px;font-size:13px;color:var(--teal,#0e9a89);min-height:18px}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);

  var modal = document.createElement("div");
  modal.id = "pr-modal";
  modal.innerHTML =
    '<div class="pr-card pr-wrap">' +
    '<span class="pr-x" id="pr-close">×</span>' +
    "<h3>Sign in</h3>" +
    "<p>No password. Enter your email and we'll send a one-time sign-in link. " +
    "First time? An account with a random nickname is created for you.</p>" +
    '<input id="pr-email" type="email" placeholder="you@example.com" autocomplete="email" />' +
    '<button id="pr-send">Send me a link</button>' +
    '<div class="pr-msg" id="pr-msg"></div>' +
    "</div>";
  document.body.appendChild(modal);

  function open() { modal.classList.add("on"); var e = document.getElementById("pr-email"); if (e) e.focus(); }
  function close() { modal.classList.remove("on"); document.getElementById("pr-msg").textContent = ""; }
  document.getElementById("pr-close").onclick = close;
  modal.addEventListener("click", function (ev) { if (ev.target === modal) close(); });

  async function send() {
    var email = (document.getElementById("pr-email").value || "").trim();
    var msg = document.getElementById("pr-msg");
    if (!email || email.indexOf("@") < 1) { msg.style.color = "var(--red,#e0442e)"; msg.textContent = "Enter a valid email."; return; }
    msg.style.color = "var(--muted,#8a7b66)"; msg.textContent = "Sending…";
    try {
      var r = await fetch(API + "/start", {
        method: "POST", headers: { "Content-Type": "application/json" },
        credentials: "include", body: JSON.stringify({ email: email }),
      });
      msg.style.color = "var(--teal,#0e9a89)";
      msg.textContent = r.ok ? "✓ Check your email for the sign-in link." : "Something went wrong — try again.";
    } catch (e) { msg.style.color = "var(--red,#e0442e)"; msg.textContent = "Network error — is the server up?"; }
  }
  document.getElementById("pr-send").onclick = send;
  document.getElementById("pr-email").addEventListener("keydown", function (e) { if (e.key === "Enter") send(); });

  async function logout(e) {
    if (e) e.preventDefault();
    try { await fetch(API + "/logout", { method: "POST", credentials: "include" }); } catch (_) {}
    refresh();
  }

  async function refresh() {
    var slot = document.getElementById("pr-auth-slot");
    if (!slot) return;
    try {
      var r = await fetch(API + "/me", { credentials: "include" });
      if (r.ok) {
        var u = await r.json();
        slot.innerHTML = '<span class="pr-nick">🎮 ' + u.nickname + '</span> <a id="pr-logout">logout</a>';
        document.getElementById("pr-logout").onclick = logout;
        return;
      }
    } catch (_) {}
    slot.innerHTML = '<a id="pr-signin">Sign in</a>';
    document.getElementById("pr-signin").onclick = function (e) { e.preventDefault(); open(); };
  }

  refresh();
})();
