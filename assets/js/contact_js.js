function toggleFaq(el) {
  el.classList.toggle('open');
}
function updateCount() {
  const val = document.getElementById('msgInput').value.length;
  document.getElementById('charCount').textContent = val;
}