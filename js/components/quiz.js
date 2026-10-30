/**
 * Interactive History Quiz Component - History of India
 * Powered by Python backend API (/api/quiz) on localhost, with offline fallback.
 */

window.HistoryApp = window.HistoryApp || {};

window.HistoryApp.Quiz = (function() {
  let questions = [];
  let currentQuestionIndex = 0;
  let userScore = 0;
  let hasAnswered = false;

  const fallbackQuestions = [
    {
      id: 1,
      question: "Which ancient Indus Valley city featured a massive tidal dockyard connected to the Arabian Sea?",
      options: ["Mohenjo-daro", "Lothal", "Harappa", "Kalibangan"],
      answer: 1,
      explanation: "Lothal in modern Gujarat had the world's earliest known tidal dockyard, facilitating trade with Mesopotamia and ancient Egypt."
    },
    {
      id: 2,
      question: "Which Mauryan Emperor renounced warfare and adopted Dhamma after the Kalinga War?",
      options: ["Chandragupta Maurya", "Bindusara", "Ashoka the Great", "Brihadratha"],
      answer: 2,
      explanation: "Emperor Ashoka experienced a profound transformation following the devastation of the Kalinga War in 261 BCE, dedicating his reign to moral governance."
    },
    {
      id: 3,
      question: "Who composed the mathematical treatise 'Aryabhatiya' calculating the approximation of Pi and heliocentric principles?",
      options: ["Aryabhata", "Varahamihira", "Brahmagupta", "Bhaskara II"],
      answer: 0,
      explanation: "Aryabhata composed the Aryabhatiya in 499 CE during the Gupta Golden Age, asserting that the Earth rotates on its axis."
    },
    {
      id: 4,
      question: "The Brihadisvara Temple at Thanjavur was consecrated in 1010 CE by which prominent monarch?",
      options: ["Rajendra Chola I", "Raja Raja Chola I", "Krishnadevaraya", "Kulothunga Chola"],
      answer: 1,
      explanation: "Raja Raja Chola I commissioned the colossal granite Vimana tower topped with an 80-tonne single granite capstone without binding mortar."
    },
    {
      id: 5,
      question: "The famous 1930 Dandi Salt March led by Mahatma Gandhi covered approximately what distance?",
      options: ["100 km", "240 miles (390 km)", "500 miles", "50 km"],
      answer: 1,
      explanation: "Mahatma Gandhi and 78 volunteers marched 240 miles from Sabarmati Ashram to the coastal village of Dandi to defy the colonial salt monopoly."
    }
  ];

  async function loadQuestions() {
    try {
      const res = await fetch('/api/quiz');
      if (res.ok) {
        const data = await res.json();
        questions = data.questions || fallbackQuestions;
        return;
      }
    } catch (e) {
      // Offline / file:/// fallback
    }
    questions = fallbackQuestions;
  }

  async function openQuizModal() {
    await loadQuestions();
    currentQuestionIndex = 0;
    userScore = 0;
    hasAnswered = false;

    const modal = document.getElementById('global-modal');
    const modalContent = document.getElementById('modal-dynamic-content');
    if (!modal || !modalContent) return;

    renderQuestion();
    modal.classList.add('active');
  }

  function renderQuestion() {
    const modalContent = document.getElementById('modal-dynamic-content');
    if (!modalContent) return;

    if (currentQuestionIndex >= questions.length) {
      renderQuizResults(modalContent);
      return;
    }

    const q = questions[currentQuestionIndex];
    hasAnswered = false;

    modalContent.innerHTML = `
      <div class="modal-card" style="grid-template-columns: 1fr; max-width: 680px; padding: 2.5rem;">
        <button class="modal-close-btn" onclick="HistoryApp.closeModal()">✕</button>
        
        <div class="flex-between" style="margin-bottom: 1.5rem;">
          <span class="badge badge-gold">Question ${currentQuestionIndex + 1} of ${questions.length}</span>
          <span style="font-family: var(--font-mono); font-size: 0.85rem; color: var(--text-tertiary);">Score: ${userScore}</span>
        </div>

        <h3 style="font-size: 1.4rem; margin-bottom: 1.8rem; line-height: 1.35; color: #ffffff;">${q.question}</h3>

        <div style="display: flex; flex-direction: column; gap: 0.85rem; margin-bottom: 1.8rem;" id="quiz-options-list">
          ${q.options.map((opt, idx) => `
            <button class="btn btn-outline quiz-option-btn" 
                    id="quiz-opt-${idx}"
                    style="justify-content: flex-start; text-align: left; padding: 1rem 1.25rem; font-size: 0.95rem; border-radius: var(--radius-xs);"
                    onclick="HistoryApp.Quiz.selectAnswer(${idx})">
              <span style="width: 26px; height: 26px; border-radius: 50%; border: var(--border-subtle); display: inline-flex; align-items: center; justify-content: center; margin-right: 0.75rem; font-size: 0.78rem; font-family: var(--font-mono); color: var(--text-gold);">
                ${String.fromCharCode(65 + idx)}
              </span>
              <span>${opt}</span>
            </button>
          `).join('')}
        </div>

        <div id="quiz-feedback" style="display: none; padding: 1.2rem; background: var(--bg-card); border-radius: var(--radius-xs); border: var(--border-subtle); margin-bottom: 1.5rem;"></div>

        <div class="flex-between" style="border-top: var(--border-subtle); padding-top: 1.2rem;">
          <span style="font-size: 0.78rem; color: var(--text-tertiary);">Python REST API Engine · Localhost 8000</span>
          <button id="quiz-next-btn" class="btn btn-primary" style="display: none;" onclick="HistoryApp.Quiz.nextQuestion()">Next Question →</button>
        </div>
      </div>
    `;
  }

  function selectAnswer(selectedIndex) {
    if (hasAnswered) return;
    hasAnswered = true;

    const q = questions[currentQuestionIndex];
    const isCorrect = selectedIndex === q.answer;
    if (isCorrect) userScore += 1;

    const feedbackEl = document.getElementById('quiz-feedback');
    const nextBtn = document.getElementById('quiz-next-btn');

    // Highlight options
    q.options.forEach((_, idx) => {
      const btn = document.getElementById(`quiz-opt-${idx}`);
      if (!btn) return;
      btn.style.pointerEvents = 'none';

      if (idx === q.answer) {
        btn.style.borderColor = '#4ade80';
        btn.style.background = 'rgba(74, 222, 128, 0.12)';
        btn.style.color = '#ffffff';
      } else if (idx === selectedIndex) {
        btn.style.borderColor = '#f87171';
        btn.style.background = 'rgba(248, 113, 113, 0.12)';
      } else {
        btn.style.opacity = '0.5';
      }
    });

    if (feedbackEl) {
      feedbackEl.style.display = 'block';
      feedbackEl.innerHTML = `
        <div style="font-weight: 600; color: ${isCorrect ? '#4ade80' : '#f87171'}; margin-bottom: 0.4rem;">
          ${isCorrect ? '✓ Correct!' : '✕ Incorrect'}
        </div>
        <p style="font-size: 0.88rem; color: var(--text-secondary); margin: 0;">${q.explanation}</p>
      `;
    }

    if (nextBtn) {
      nextBtn.style.display = 'inline-flex';
    }
  }

  function nextQuestion() {
    currentQuestionIndex++;
    renderQuestion();
  }

  function renderQuizResults(modalContent) {
    const percentage = Math.round((userScore / questions.length) * 100);
    modalContent.innerHTML = `
      <div class="modal-card" style="grid-template-columns: 1fr; max-width: 580px; padding: 3rem 2.5rem; text-align: center;">
        <button class="modal-close-btn" onclick="HistoryApp.closeModal()">✕</button>
        
        <div style="font-size: 3rem; margin-bottom: 1rem;">🏆</div>
        <span class="badge badge-gold" style="margin-bottom: 1rem;">Challenge Complete</span>
        <h2 style="font-size: 2.2rem; margin-bottom: 0.5rem;">${userScore} / ${questions.length} Correct</h2>
        <p style="font-size: 1.1rem; color: var(--text-gold); margin-bottom: 1.5rem;">Knowledge Mastery: ${percentage}%</p>
        
        <p style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 2.5rem; line-height: 1.6;">
          ${percentage >= 80 
            ? 'Exceptional mastery of Indian civilizational heritage, architecture, and statecraft!' 
            : 'A commendable expedition into India\'s rich history. Revisit the eras to master more milestones!'}
        </p>

        <div style="display: flex; gap: 1rem; justify-content: center;">
          <button class="btn btn-primary" onclick="HistoryApp.Quiz.openQuizModal()">Retake Challenge</button>
          <button class="btn btn-outline" onclick="HistoryApp.closeModal()">Back to Archive</button>
        </div>
      </div>
    `;
  }

  return {
    openQuizModal: openQuizModal,
    selectAnswer: selectAnswer,
    nextQuestion: nextQuestion
  };
})();
