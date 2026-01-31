(() => {
    const existing = document.getElementById('starfield-canvas');
    const canvas = existing || document.createElement('canvas');
    canvas.id = 'starfield-canvas';
    if (!existing) document.body.prepend(canvas);

    const ctx = canvas.getContext('2d');
    let width = 0;
    let height = 0;
    let centerX = 0;
    let centerY = 0;

    const starCount = 140;
    const stars = [];

    const settings = {
        depth: 900,
        baseSpeed: 0.22,
        drift: 0.08,
        fallBias: 0.35,
        parallax: 6
    };

    let targetPx = 0;
    let targetPy = 0;
    let currentPx = 0;
    let currentPy = 0;

    function resize() {
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        width = window.innerWidth;
        height = window.innerHeight;
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        canvas.style.width = `${width}px`;
        canvas.style.height = `${height}px`;
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        centerX = width / 2;
        centerY = height / 2;
    }

    function createStar() {
        return {
            x: (Math.random() - 0.5) * width,
            y: (Math.random() - 0.5) * height,
            z: Math.random() * settings.depth + 120,
            size: Math.random() * 1.4 + 0.4,
            speed: Math.random() * 0.4 + settings.baseSpeed,
            alpha: Math.random() * 0.5 + 0.2
        };
    }

    function resetStar(star) {
        star.x = (Math.random() - 0.5) * width;
        star.y = (Math.random() - 0.5) * height;
        star.z = settings.depth + Math.random() * 300;
        star.size = Math.random() * 1.4 + 0.4;
        star.speed = Math.random() * 0.4 + settings.baseSpeed;
        star.alpha = Math.random() * 0.5 + 0.2;
    }

    function init() {
        stars.length = 0;
        for (let i = 0; i < starCount; i++) {
            stars.push(createStar());
        }
    }

    function draw() {
        ctx.clearRect(0, 0, width, height);

        currentPx += (targetPx - currentPx) * 0.04;
        currentPy += (targetPy - currentPy) * 0.04;
        const px = currentPx * settings.parallax;
        const py = currentPy * settings.parallax;

        for (const star of stars) {
            star.y += star.speed + settings.fallBias;
            star.x += settings.drift * (0.5 - Math.random());
            star.z -= star.speed * 0.4;

            if (star.y > height / 2 + 60 || star.z < 60) {
                resetStar(star);
                star.y = -height / 2 - Math.random() * 60;
            }

            const scale = settings.depth / star.z;
            const x = star.x * scale + centerX + px * scale;
            const y = star.y * scale + centerY + py * scale;
            const radius = star.size * scale;

            if (x < -50 || x > width + 50 || y < -50 || y > height + 50) continue;

            const glow = Math.max(0.08, star.alpha * (scale * 0.6));
            ctx.beginPath();
            ctx.fillStyle = `rgba(140, 200, 255, ${glow})`;
            ctx.arc(x, y, radius, 0, Math.PI * 2);
            ctx.fill();
        }

        requestAnimationFrame(draw);
    }

    window.addEventListener('mousemove', (event) => {
        targetPx = (event.clientX / window.innerWidth) - 0.5;
        targetPy = (event.clientY / window.innerHeight) - 0.5;
    }, { passive: true });

    window.addEventListener('resize', () => {
        resize();
        init();
    });

    resize();
    init();
    requestAnimationFrame(draw);
})();