// sidenav for dashboard

let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".sidebarBtn");

function toggleSidebar() {
  sidebar.classList.toggle("active");

  if (sidebar.classList.contains("active")) {
    sidebarBtn.classList.replace("bx-menu", "bx-menu-alt-right");
    if (window.innerWidth < 601) {
      sidebar.style.display = "block";
    }
  } else {
    sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
    sidebar.style.display = "none";
  }
}

sidebarBtn.addEventListener("click", toggleSidebar);

window.addEventListener("resize", function() {
  if (window.innerWidth > 600) {
    sidebar.style.display = "block";
  }
  else {
    sidebarBtn.classList.replace("bx-menu-alt-right", "bx-menu");
    sidebar.style.display = "none";
  }
});



