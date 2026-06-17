// Chain pill selection
document.querySelectorAll('.chain-pill').forEach(pill => {
  pill.addEventListener('click', () => {
    const group = pill.closest('.chain-picker');
    group.querySelectorAll('.chain-pill').forEach(p => p.classList.remove('active'));
    pill.classList.add('active');
  });
});
