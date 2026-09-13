(function () {
  "use strict";

  // ---- Tema claro/oscuro, con memoria ----
  var root = document.documentElement;
  var saved = null;
  try { saved = localStorage.getItem("theme"); } catch (e) {}
  if (saved === "light" || saved === "dark") root.setAttribute("data-theme", saved);

  function currentTheme() {
    var attr = root.getAttribute("data-theme");
    if (attr) return attr;
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function applyToggleLabel(btn) {
    btn.textContent = currentTheme() === "dark" ? "☀️" : "🌙";
    btn.setAttribute("aria-label", currentTheme() === "dark" ? "Cambiar a modo claro" : "Cambiar a modo oscuro");
  }

  document.addEventListener("DOMContentLoaded", function () {
    var toggle = document.getElementById("theme-toggle");
    if (toggle) {
      applyToggleLabel(toggle);
      toggle.addEventListener("click", function () {
        var next = currentTheme() === "dark" ? "light" : "dark";
        root.setAttribute("data-theme", next);
        try { localStorage.setItem("theme", next); } catch (e) {}
        applyToggleLabel(toggle);
      });
    }

    // ---- Sidebar móvil ----
    var menuBtn = document.getElementById("menu-toggle");
    var sidebar = document.getElementById("sidebar");
    var overlay = document.getElementById("sidebar-overlay");
    function closeSidebar() {
      if (sidebar) sidebar.classList.remove("open");
      if (overlay) overlay.classList.remove("open");
    }
    if (menuBtn && sidebar) {
      menuBtn.addEventListener("click", function () {
        sidebar.classList.toggle("open");
        if (overlay) overlay.classList.toggle("open");
      });
    }
    if (overlay) overlay.addEventListener("click", closeSidebar);

    // Cierra la sidebar móvil al elegir una página
    if (sidebar) {
      sidebar.querySelectorAll("a").forEach(function (a) {
        a.addEventListener("click", closeSidebar);
      });
    }
  });
})();
