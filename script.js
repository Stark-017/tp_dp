// ===== BTS BIRTHDAY INTERACTIVE SCRIPT FOR DEVHUTI ===== //
document.addEventListener('DOMContentLoaded', () => {
    initScrollReveal();
    initHearts();
    initAudioEngine();
    initCakeBlow();
    initArmyBomb();
    initConfetti();
    initClickRipples();
});

/* 1. SCROLL REVEAL OBSERVER FOR DUAL MEMBER CARDS */
function initScrollReveal() {
    const cards = document.querySelectorAll('.member-card');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('card-revealed');
                // Trigger a mini confetti burst whenever a new member card enters
                burstConfetti(entry.target.getBoundingClientRect().left + 150, entry.target.getBoundingClientRect().top + 100, 15);
            }
        });
    }, {
        threshold: 0.25,
        rootMargin: '0px 0px -50px 0px'
    });

    cards.forEach(card => observer.observe(card));
}

/* 2. FLOATING PURPLE HEARTS GENERATOR */
function initHearts() {
    const heartContainer = document.getElementById('heart-container');
    const heartIcons = ['💜', '✨', '🌸', '💖', '⭐', '🎂', '🥳'];

    function createHeart() {
        if (!heartContainer) return;
        const heart = document.createElement('div');
        heart.classList.add('floating-heart');
        heart.innerText = heartIcons[Math.floor(Math.random() * heartIcons.length)];
        
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.animationDuration = (8 + Math.random() * 8) + 's';
        heart.style.fontSize = (16 + Math.random() * 22) + 'px';
        
        heartContainer.appendChild(heart);

        setTimeout(() => {
            heart.remove();
        }, 16000);
    }

    // Spawn initial hearts & interval
    for (let i = 0; i < 15; i++) {
        setTimeout(createHeart, i * 400);
    }
    setInterval(createHeart, 800);
}

/* 3. WEB AUDIO API SYNTHESIZER - PLAYS BTS BIRTHDAY MELODY */
let audioCtx = null;
let isPlaying = false;
let musicTimer = null;

function initAudioEngine() {
    const musicBtn = document.getElementById('music-toggle-btn');
    const eqBars = document.getElementById('eq-bars');
    const musicLabel = document.getElementById('music-label');
    const musicIcon = document.getElementById('music-icon');

    if (!musicBtn) return;

    musicBtn.addEventListener('click', () => {
        if (!isPlaying) {
            startMelody();
            eqBars.classList.add('playing');
            musicLabel.innerText = "Playing Borahae Melody 💜";
            musicIcon.innerText = "⏸️";
            isPlaying = true;
        } else {
            stopMelody();
            eqBars.classList.remove('playing');
            musicLabel.innerText = "Play BTS Birthday Melody";
            musicIcon.innerText = "🎵";
            isPlaying = false;
        }
    });
}

function startMelody() {
    if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    }
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }

    // Notes for "Happy Birthday to Devhuti" BTS Lofi Chords
    // Frequencies (Hz)
    const N = {
        C4: 261.63, D4: 293.66, E4: 329.63, F4: 349.23, G4: 392.00, A4: 440.00, B4: 493.88,
        C5: 523.25, D5: 587.33, E5: 659.25, F5: 698.46, G5: 783.99, A5: 880.00
    };

    const melody = [
        { note: N.C4, dur: 0.3 }, { note: N.C4, dur: 0.3 }, { note: N.D4, dur: 0.6 }, { note: N.C4, dur: 0.6 }, { note: N.F4, dur: 0.6 }, { note: N.E4, dur: 1.0 },
        { note: N.C4, dur: 0.3 }, { note: N.C4, dur: 0.3 }, { note: N.D4, dur: 0.6 }, { note: N.C4, dur: 0.6 }, { note: N.G4, dur: 0.6 }, { note: N.F4, dur: 1.0 },
        { note: N.C4, dur: 0.3 }, { note: N.C4, dur: 0.3 }, { note: N.C5, dur: 0.6 }, { note: N.A4, dur: 0.6 }, { note: N.F4, dur: 0.6 }, { note: N.E4, dur: 0.6 }, { note: N.D4, dur: 0.8 },
        { note: N.A4, dur: 0.3 }, { note: N.A4, dur: 0.3 }, { note: N.A4, dur: 0.6 }, { note: N.F4, dur: 0.6 }, { note: N.G4, dur: 0.6 }, { note: N.F4, dur: 1.4 }
    ];

    let index = 0;

    function playNext() {
        if (!isPlaying) return;
        const current = melody[index];
        playSynthesizedTone(current.note, current.dur * 0.9);
        
        index = (index + 1) % melody.length;
        musicTimer = setTimeout(playNext, current.dur * 1000);
    }

    playNext();
}

function stopMelody() {
    if (musicTimer) clearTimeout(musicTimer);
}

function playSynthesizedTone(freq, duration) {
    if (!audioCtx) return;
    try {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        
        // Warm BTS electric piano / synth timbre
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

        gain.gain.setValueAtTime(0.001, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.18, audioCtx.currentTime + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);

        osc.connect(gain);
        gain.connect(audioCtx.destination);

        osc.start();
        osc.stop(audioCtx.currentTime + duration);
    } catch (e) {
        console.log(e);
    }
}

/* 4. INTERACTIVE CAKE CANDLES BLOW-OUT */
function initCakeBlow() {
    const cakeStage = document.getElementById('cake-stage');
    const blowBtn = document.getElementById('blow-candles-btn');
    const flames = document.querySelectorAll('.flame');
    const wishMsg = document.getElementById('wish-revealed');
    let blownOut = false;

    function blowOutCandles() {
        if (blownOut) return;
        blownOut = true;

        flames.forEach((flame, idx) => {
            setTimeout(() => {
                flame.classList.add('blown-out');
            }, idx * 150);
        });

        if (blowBtn) {
            blowBtn.innerHTML = "✨ Wish Granted! Borahae Devhuti! 💜✨";
            blowBtn.style.background = "linear-gradient(135deg, #10b981, #6366f1)";
        }

        if (wishMsg) {
            wishMsg.classList.remove('hidden');
        }

        // Mega confetti & fireworks blast
        for (let i = 0; i < 8; i++) {
            setTimeout(() => {
                triggerMegaConfetti();
            }, i * 350);
        }
    }

    if (cakeStage) cakeStage.addEventListener('click', blowOutCandles);
    if (blowBtn) blowBtn.addEventListener('click', blowOutCandles);
}

/* 5. ARMY BOMB FAB ACTION */
function initArmyBomb() {
    const bombBtn = document.getElementById('army-bomb-btn');
    if (!bombBtn) return;

    bombBtn.addEventListener('click', () => {
        triggerMegaConfetti();
        // Flash screen with purple glow
        const flash = document.createElement('div');
        flash.style.position = 'fixed';
        flash.style.top = '0';
        flash.style.left = '0';
        flash.style.width = '100vw';
        flash.style.height = '100vh';
        flash.style.background = 'radial-gradient(circle, rgba(192, 132, 252, 0.4) 0%, transparent 80%)';
        flash.style.pointerEvents = 'none';
        flash.style.zIndex = '9999';
        flash.style.transition = 'opacity 0.8s ease';
        document.body.appendChild(flash);

        setTimeout(() => {
            flash.style.opacity = '0';
            setTimeout(() => flash.remove(), 800);
        }, 100);
    });
}

/* 6. CONFETTI CANVAS ENGINE */
let confettiParticles = [];
const confettiColors = ['#8b5cf6', '#c084fc', '#e9d5ff', '#ec4899', '#f472b6', '#fbbf24', '#ffffff'];

function initConfetti() {
    const canvas = document.getElementById('confetti-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');

    function resize() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    function loop() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        for (let i = 0; i < confettiParticles.length; i++) {
            const p = confettiParticles[i];
            p.x += p.vx;
            p.y += p.vy;
            p.vy += 0.15; // gravity
            p.rotation += p.vRot;
            p.opacity -= 0.008;

            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.rotate(p.rotation);
            ctx.fillStyle = p.color;
            ctx.globalAlpha = Math.max(0, p.opacity);
            ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 0.6);
            ctx.restore();
        }

        confettiParticles = confettiParticles.filter(p => p.opacity > 0 && p.y < canvas.height + 50);
        requestAnimationFrame(loop);
    }
    loop();

    // Initial welcome burst
    setTimeout(() => {
        triggerMegaConfetti();
    }, 600);
}

function burstConfetti(x, y, count = 30) {
    for (let i = 0; i < count; i++) {
        confettiParticles.push({
            x: x,
            y: y,
            size: 6 + Math.random() * 8,
            color: confettiColors[Math.floor(Math.random() * confettiColors.length)],
            vx: (Math.random() - 0.5) * 12,
            vy: (Math.random() - 1.2) * 10,
            rotation: Math.random() * Math.PI * 2,
            vRot: (Math.random() - 0.5) * 0.2,
            opacity: 1
        });
    }
}

function triggerMegaConfetti() {
    burstConfetti(window.innerWidth * 0.2, window.innerHeight * 0.4, 40);
    burstConfetti(window.innerWidth * 0.5, window.innerHeight * 0.3, 60);
    burstConfetti(window.innerWidth * 0.8, window.innerHeight * 0.4, 40);
}

/* 7. CLICK RIPPLE PURPLE HEARTS */
function initClickRipples() {
    window.addEventListener('click', (e) => {
        // Prevent on interactive buttons
        if (e.target.closest('button') || e.target.closest('#interactive-cake')) return;

        const ripple = document.createElement('div');
        ripple.innerText = '💜';
        ripple.style.position = 'fixed';
        ripple.style.left = (e.clientX - 12) + 'px';
        ripple.style.top = (e.clientY - 12) + 'px';
        ripple.style.fontSize = '24px';
        ripple.style.pointerEvents = 'none';
        ripple.style.zIndex = '9999';
        ripple.style.transition = 'all 0.8s cubic-bezier(0.16, 1, 0.3, 1)';
        ripple.style.transform = 'scale(0.5)';
        ripple.style.opacity = '1';

        document.body.appendChild(ripple);

        requestAnimationFrame(() => {
            ripple.style.transform = 'scale(2.2) translateY(-40px)';
            ripple.style.opacity = '0';
        });

        setTimeout(() => {
            ripple.remove();
        }, 850);
    });
}
