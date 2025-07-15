// ASET/JS/SCRIPT.JS

// Menunggu seluruh konten halaman dimuat sebelum menjalankan skrip
document.addEventListener("DOMContentLoaded", function () {
  // --- Efek Mengetik (Typing Effect) pada Hero Section ---
  const typedEl = document.getElementById("typed-text");
  if (typedEl) {
    const fullText = "hi, antonius riki hermawan here.";
    let index = 0;

    function type() {
      if (index < fullText.length) {
        const char = fullText.charAt(index);
        let htmlToAdd = char;

        // Memberi warna putih pada "hi," dan "here."
        if ((index >= 0 && index <= 2) || (index >= 27 && index <= 31)) {
          htmlToAdd = `<span style="color: white;">${char}</span>`;
        }
        // Memberi efek tebal pada nama
        else if (index >= 4 && index <= 26) {
          htmlToAdd = `<span style="font-weight: bold;">${char}</span>`;
        }

        typedEl.innerHTML += htmlToAdd;
        index++;
        setTimeout(type, 100);
      }
    }
    // Memulai efek mengetik
    type();
  }

  // --- Logika Showcase Project ---
  const projects = [
    {
      title: "Clone Website Dicoding",
      image: "/static/assets/image/project1.png",
      link: "https://github.com/antoniusrikihermawan",
    },
    {
      title: "Bali Travel",
      image: "/static/assets/image/project2.png",
      link: "https://github.com/antoniusrikihermawan/UAS-CSP.git",
    },
    {
      title: "Portofolio Website",
      image: "/static/assets/image/project3.png",
      link: "https://github.com/antoniusrikihermawan/portofolio-ytCodehal.git",
    },
  ];

  let currentIndex = 0;
  const showcaseImg = document.getElementById("showcase-img");
  const showcaseTitle = document.getElementById("showcase-title");
  const showcaseLink = document.getElementById("showcase-link");

  function updateShowcase() {
    if (showcaseImg) {
      // Hanya berjalan jika elemen showcase ada
      const project = projects[currentIndex];
      showcaseImg.src = project.image;
      showcaseTitle.textContent = project.title;
      showcaseLink.href = project.link;
    }
  }

  // Menambahkan event listener ke tombol navigasi proyek
  // Pastikan tombol ini ada di HTML Anda dengan onclick="nextProject()" dan onclick="prevProject()"
  window.nextProject = function () {
    currentIndex = (currentIndex + 1) % projects.length;
    updateShowcase();
  };

  window.prevProject = function () {
    currentIndex = (currentIndex - 1 + projects.length) % projects.length;
    updateShowcase();
  };

  // Inisialisasi showcase saat halaman pertama kali dimuat
  updateShowcase();

  // --- Animasi Scroll (Fade-in) & Navigasi Aktif ---
  // 1. Animasi Fade-in on Scroll
  const revealElements = document.querySelectorAll(".reveal");

  const revealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          revealObserver.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1 }
  );

  revealElements.forEach((el) => {
    revealObserver.observe(el);
  });

  // 2. Navigasi Aktif saat Scroll
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".navbar-nav .nav-link");

  const navObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute("id");
          navLinks.forEach((link) => {
            link.classList.remove("active");
            if (link.getAttribute("href") == `#${id}`) {
              link.classList.add("active");
            }
          });
        }
      });
    },
    { rootMargin: "-50% 0px -50% 0px" }
  );

  sections.forEach((section) => {
    navObserver.observe(section);
  });
});

// --- Fungsi Global Lainnya ---

// Fungsi untuk tombol 'Say Hi'
function sayHi() {
  alert("Thanks for reaching out! ✨");
}

// Efek latar belakang navbar saat di-scroll
// Diletakkan di luar DOMContentLoaded karena tidak bergantung pada elemen spesifik
window.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
    // Gunakan kelas yang sudah ada di CSS Anda untuk konsistensi
    // Anda bisa membuat kelas baru misal .navbar-scrolled
    navbar.style.backgroundColor = "rgba(13, 23, 42, 0.85)";
  } else {
    navbar.style.backgroundColor = "rgba(0, 0, 0, 0.2)";
  }
});

function showCertificateModal(title, issuer, description, fileUrl, type) {
  document.getElementById("modalTitle").innerText = title;
  document.getElementById("modalIssuer").innerText = issuer;
  document.getElementById("modalDescription").innerText = description;

  const container = document.getElementById("modalImageContainer");
  container.innerHTML = ""; // Clear previous content

  if (type === "image") {
    const img = document.createElement("img");
    img.src = fileUrl;
    img.alt = title;
    img.className = "img-fluid rounded shadow";
    container.appendChild(img);
  } else if (type === "pdf") {
    const embed = document.createElement("embed");
    embed.src = fileUrl;
    embed.type = "application/pdf";
    embed.width = "100%";
    embed.height = "500px";
    embed.className = "rounded shadow";
    container.appendChild(embed);
  }
}
