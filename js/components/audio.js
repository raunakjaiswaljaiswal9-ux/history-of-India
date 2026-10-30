/**
 * Ambient Drone Synthesizer - History of India
 * Zero-dependency Web Audio API implementation generating an authentic,
 * meditative Tanpura harmonic drone (Sa - Pa Indian classical tuning).
 */

window.HistoryApp = window.HistoryApp || {};

window.HistoryApp.Audio = (function() {
  let audioCtx = null;
  let isPlaying = false;
  let masterGain = null;
  let oscillators = [];

  function init() {
    const toggleBtn = document.getElementById('ambient-audio-toggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', togglePlay);
    }
  }

  function startDrone() {
    if (!audioCtx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      audioCtx = new AudioContext();
    }

    if (audioCtx.state === 'suspended') {
      audioCtx.resume();
    }

    masterGain = audioCtx.createGain();
    masterGain.gain.setValueAtTime(0.001, audioCtx.currentTime);
    masterGain.gain.exponentialRampToValueAtTime(0.12, audioCtx.currentTime + 2.5); // Soft ramp-up
    masterGain.connect(audioCtx.destination);

    // Fundamental frequencies: Sa (C#3 / 138.59 Hz), Pa (G#3 / 207.65 Hz), Upper Sa (277.18 Hz)
    const baseFreqs = [138.59, 207.65, 277.18, 554.37];

    oscillators = baseFreqs.map((freq, index) => {
      const osc = audioCtx.createOscillator();
      const oscGain = audioCtx.createGain();
      
      // Triangle & Sine waves create smooth harmonic overtones like plucked bronze strings
      osc.type = index % 2 === 0 ? 'sine' : 'triangle';
      osc.frequency.setValueAtTime(freq, audioCtx.currentTime);

      // Subtle detuning for natural shimmer / chorus
      osc.detune.setValueAtTime((index - 1.5) * 4, audioCtx.currentTime);

      // Low pass filter to remove harsh highs
      const filter = audioCtx.createBiquadFilter();
      filter.type = 'lowpass';
      filter.frequency.setValueAtTime(800, audioCtx.currentTime);

      const level = (1 / (index + 1)) * 0.4;
      oscGain.gain.setValueAtTime(level, audioCtx.currentTime);

      osc.connect(filter);
      filter.connect(oscGain);
      oscGain.connect(masterGain);

      osc.start();
      return osc;
    });

    isPlaying = true;
    updateUI(true);
  }

  function stopDrone() {
    if (!audioCtx || !masterGain) return;

    masterGain.gain.setValueAtTime(masterGain.gain.value, audioCtx.currentTime);
    masterGain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + 1.2);

    setTimeout(() => {
      oscillators.forEach(osc => {
        try { osc.stop(); osc.disconnect(); } catch (e) {}
      });
      oscillators = [];
      isPlaying = false;
      updateUI(false);
    }, 1300);
  }

  function togglePlay() {
    if (isPlaying) {
      stopDrone();
    } else {
      startDrone();
    }
  }

  function updateUI(playing) {
    const toggleBtn = document.getElementById('ambient-audio-toggle');
    if (!toggleBtn) return;

    if (playing) {
      toggleBtn.classList.add('playing');
      const label = toggleBtn.querySelector('.label-text');
      if (label) label.textContent = 'Atmosphere: On';
    } else {
      toggleBtn.classList.remove('playing');
      const label = toggleBtn.querySelector('.label-text');
      if (label) label.textContent = 'Atmosphere';
    }
  }

  return {
    init: init,
    togglePlay: togglePlay
  };
})();
