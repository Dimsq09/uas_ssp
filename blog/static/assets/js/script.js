// Updated JavaScript for dynamic projects from database
document.addEventListener("DOMContentLoaded", function () {
  // --- Efek Mengetik (Typing Effect) pada Hero Section ---
  const typedEl = document.getElementById("typed-text");
  if (typedEl) {
    const fullText = "Hai, Aku Dhimaz Satrya!";
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

  // --- Dynamic Project Showcase Logic ---
  // Get featured projects from Django template (passed as JSON)
  const featuredProjectsData = document.getElementById('featured-projects-data');
  let projects = [];
  
  if (featuredProjectsData) {
    try {
      projects = JSON.parse(featuredProjectsData.textContent);
    } catch (e) {
      console.error('Error parsing featured projects data:', e);
      projects = [];
    }
  }

  let currentIndex = 0;
  const showcaseImg = document.getElementById("showcase-img");
  const showcaseTitle = document.getElementById("showcase-title");
  const showcaseDescription = document.getElementById("showcase-description");
  const showcaseTechnologies = document.getElementById("showcase-technologies");
  const showcaseLink = document.getElementById("showcase-link");

  function updateShowcase() {
    if (showcaseImg && projects.length > 0) {
      const project = projects[currentIndex];
      showcaseImg.src = project.image;
      showcaseImg.alt = project.title;
      showcaseTitle.textContent = project.title;
      
      if (showcaseDescription) {
        showcaseDescription.textContent = project.description;
      }
      
      if (showcaseTechnologies) {
        showcaseTechnologies.textContent = project.technologies;
      }
      
      if (showcaseLink && project.github_link) {
        showcaseLink.href = project.github_link;
        showcaseLink.style.display = 'inline-block';
      } else if (showcaseLink) {
        showcaseLink.style.display = 'none';
      }
    }
  }

  // Navigation functions for project carousel
  window.nextProject = function () {
    if (projects.length > 1) {
      currentIndex = (currentIndex + 1) % projects.length;
      updateShowcase();
    }
  };

  window.prevProject = function () {
    if (projects.length > 1) {
      currentIndex = (currentIndex - 1 + projects.length) % projects.length;
      updateShowcase();
    }
  };

  // Auto-slide projects every 5 seconds
  if (projects.length > 1) {
    setInterval(() => {
      window.nextProject();
    }, 5000);
  }

  // Initialize showcase
  updateShowcase();

  // --- Existing code for animations and other features ---
  // ... (keep all your existing code for typing effect, scroll animations, etc.)
  
  // --- Animasi Scroll (Fade-in) & Navigasi Aktif ---
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

  // Navigation active state on scroll
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

// --- Global Functions ---
function sayHi() {
  alert("Thanks for reaching out! ✨");
}

// Navbar background effect on scroll
window.addEventListener("scroll", function () {
  const navbar = document.querySelector(".navbar");
  if (window.scrollY > 50) {
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
  container.innerHTML = "";

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