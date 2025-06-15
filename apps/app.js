// Application data
const appData = {
  ticket_medio: 42.90,
  social_manager_tiers: {
    140: {name: "Silver", posts: 8, roi_bonus: 0},
    380: {name: "Golden", posts: 12, roi_bonus: 5},
    590: {name: "Diamond", posts: 12, roi_bonus: 10}
  },
  servizi_opzionali: {
    "TikTok Marketing": {costo: 300, roi_bonus: 8, clienti_bonus: 5},
    "LinkedIn Business": {costo: 200, roi_bonus: 3, clienti_bonus: 2},
    "Email Marketing": {costo: 150, roi_bonus: 5, clienti_bonus: 3},
    "Sistema CRM": {costo: 400, roi_bonus: 10, clienti_bonus: 4}
  },
  baseline_roi: 30,
  baseline_clienti_mese: 8,
  fasi_crescita: [0.5, 0.75, 1.0, 1.0],
  competitor_data: {
    budget_medio_mercato: 1200,
    roi_medio_mercato: 25,
    clienti_medi_mercato: 12
  }
};

// Application state
let currentParams = {
  socialManagerBudget: 380,
  advertisingBudget: 800,
  contentBudget: 3000,
  influencerBudget: 2000,
  projectDuration: 6,
  optionalServices: []
};

// Chart instance
let costChart = null;

// DOM elements
const elements = {
  socialManagerSlider: document.getElementById('social-manager-budget'),
  advertisingSlider: document.getElementById('advertising-budget'),
  contentSlider: document.getElementById('content-budget'),
  influencerSlider: document.getElementById('influencer-budget'),
  durationSelect: document.getElementById('project-duration'),
  checkboxes: document.querySelectorAll('input[type="checkbox"]'),
  totalInvestment: document.getElementById('total-investment'),
  expectedROI: document.getElementById('expected-roi'),
  newClients: document.getElementById('new-clients'),
  additionalRevenue: document.getElementById('additional-revenue'),
  investmentBreakdown: document.getElementById('investment-breakdown'),
  roiDescription: document.getElementById('roi-description'),
  requestQuoteBtn: document.getElementById('request-quote'),
  modal: document.getElementById('quote-modal'),
  modalClose: document.querySelector('.modal-close'),
  quoteForm: document.getElementById('quote-form')
};

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
  initializeEventListeners();
  initializeChart();
  updateCalculations();
});

// Event listeners
function initializeEventListeners() {
  // Sliders
  elements.socialManagerSlider.addEventListener('input', handleSocialManagerChange);
  elements.advertisingSlider.addEventListener('input', handleAdvertisingChange);
  elements.contentSlider.addEventListener('input', handleContentChange);
  elements.influencerSlider.addEventListener('input', handleInfluencerChange);
  
  // Duration select
  elements.durationSelect.addEventListener('change', handleDurationChange);
  
  // Checkboxes
  elements.checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', handleServiceChange);
  });
  
  // Modal
  elements.requestQuoteBtn.addEventListener('click', openModal);
  elements.modalClose.addEventListener('click', closeModal);
  elements.modal.addEventListener('click', function(e) {
    if (e.target === elements.modal) closeModal();
  });
  
  // Form
  elements.quoteForm.addEventListener('submit', handleFormSubmit);
  
  // Close modal on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && elements.modal.classList.contains('active')) {
      closeModal();
    }
  });
}

// Handle input changes
function handleSocialManagerChange(e) {
  currentParams.socialManagerBudget = parseInt(e.target.value);
  updateSliderDisplay(e.target, formatCurrency(currentParams.socialManagerBudget), getSocialManagerTier(currentParams.socialManagerBudget));
  updateCalculations();
}

function handleAdvertisingChange(e) {
  currentParams.advertisingBudget = parseInt(e.target.value);
  updateSliderDisplay(e.target, formatCurrency(currentParams.advertisingBudget));
  updateCalculations();
}

function handleContentChange(e) {
  currentParams.contentBudget = parseInt(e.target.value);
  updateSliderDisplay(e.target, formatCurrency(currentParams.contentBudget));
  updateCalculations();
}

function handleInfluencerChange(e) {
  currentParams.influencerBudget = parseInt(e.target.value);
  updateSliderDisplay(e.target, formatCurrency(currentParams.influencerBudget));
  updateCalculations();
}

function handleDurationChange(e) {
  currentParams.projectDuration = parseInt(e.target.value);
  updateCalculations();
}

function handleServiceChange(e) {
  const service = e.target.value;
  if (e.target.checked) {
    if (!currentParams.optionalServices.includes(service)) {
      currentParams.optionalServices.push(service);
    }
  } else {
    currentParams.optionalServices = currentParams.optionalServices.filter(s => s !== service);
  }
  updateCalculations();
}

// Update slider display
function updateSliderDisplay(slider, value, tier = null) {
  const display = slider.nextElementSibling;
  const valueSpan = display.querySelector('.slider-value');
  const tierSpan = display.querySelector('.slider-tier');
  
  valueSpan.textContent = value;
  if (tierSpan && tier) {
    tierSpan.textContent = tier;
  }
}

// Get social manager tier
function getSocialManagerTier(budget) {
  if (budget <= 140) return appData.social_manager_tiers[140].name;
  if (budget <= 380) return appData.social_manager_tiers[380].name;
  return appData.social_manager_tiers[590].name;
}

// Calculate all metrics
function updateCalculations() {
  const calculations = calculateMetrics();
  updateUI(calculations);
  updateChart(calculations.breakdown);
}

function calculateMetrics() {
  // Calculate monthly costs
  const monthlyCost = currentParams.socialManagerBudget + currentParams.advertisingBudget;
  const optionalServicesCost = currentParams.optionalServices.reduce((total, service) => {
    return total + appData.servizi_opzionali[service].costo;
  }, 0);
  
  const totalMonthlyCost = monthlyCost + optionalServicesCost;
  const oneTimeCost = currentParams.contentBudget + currentParams.influencerBudget;
  const totalInvestment = (totalMonthlyCost * currentParams.projectDuration) + oneTimeCost;
  
  // Calculate ROI
  let roiBonus = 0;
  
  // Social manager tier bonus
  const socialTier = getSocialManagerTierData(currentParams.socialManagerBudget);
  roiBonus += socialTier.roi_bonus;
  
  // Video/content bonus
  if (currentParams.contentBudget >= 2000) roiBonus += 10;
  
  // Influencer bonus
  if (currentParams.influencerBudget >= 1500) roiBonus += 15;
  
  // High advertising budget bonus
  if (currentParams.advertisingBudget >= 1000) roiBonus += 10;
  
  // Optional services bonus
  roiBonus += currentParams.optionalServices.reduce((total, service) => {
    return total + appData.servizi_opzionali[service].roi_bonus;
  }, 0);
  
  // Threshold effects
  if (totalMonthlyCost < 800) roiBonus -= 10; // Low budget penalty
  
  const expectedROI = Math.min(appData.baseline_roi + roiBonus, 80); // Cap at 80%
  
  // Calculate new clients per month
  let newClientsBase = appData.baseline_clienti_mese;
  newClientsBase += Math.floor(currentParams.advertisingBudget / 100);
  newClientsBase += getSocialManagerTierData(currentParams.socialManagerBudget).posts / 2;
  newClientsBase += Math.floor(currentParams.influencerBudget / 500);
  
  // Optional services bonus
  newClientsBase += currentParams.optionalServices.reduce((total, service) => {
    return total + appData.servizi_opzionali[service].clienti_bonus;
  }, 0);
  
  const newClientsMonth = Math.floor(newClientsBase);
  
  // Calculate additional revenue
  const monthlyRevenue = newClientsMonth * appData.ticket_medio;
  const annualRevenue = monthlyRevenue * 12;
  
  // Apply growth phases
  const effectiveMonths = Math.min(currentParams.projectDuration, 4);
  const growthMultiplier = appData.fasi_crescita[effectiveMonths - 1] || 1.0;
  const adjustedAnnualRevenue = annualRevenue * growthMultiplier;
  
  // Cost breakdown
  const breakdown = {
    'Social Media Manager': currentParams.socialManagerBudget * currentParams.projectDuration,
    'Advertising': currentParams.advertisingBudget * currentParams.projectDuration,
    'Contenuti Video/Foto': currentParams.contentBudget,
    'Influencer Marketing': currentParams.influencerBudget,
    'Servizi Opzionali': optionalServicesCost * currentParams.projectDuration
  };
  
  return {
    totalInvestment,
    totalMonthlyCost,
    oneTimeCost,
    expectedROI,
    newClientsMonth,
    monthlyRevenue,
    annualRevenue: adjustedAnnualRevenue,
    breakdown,
    paybackMonths: Math.ceil(totalInvestment / monthlyRevenue)
  };
}

function getSocialManagerTierData(budget) {
  if (budget <= 140) return appData.social_manager_tiers[140];
  if (budget <= 380) return appData.social_manager_tiers[380];
  return appData.social_manager_tiers[590];
}

// Update UI with calculations
function updateUI(calculations) {
  // Add animation class
  elements.totalInvestment.classList.add('updating');
  elements.expectedROI.classList.add('updating');
  elements.newClients.classList.add('updating');
  elements.additionalRevenue.classList.add('updating');
  
  setTimeout(() => {
    elements.totalInvestment.textContent = formatCurrency(calculations.totalInvestment);
    elements.expectedROI.textContent = `${calculations.expectedROI}%`;
    elements.newClients.textContent = calculations.newClientsMonth;
    elements.additionalRevenue.textContent = formatCurrency(calculations.annualRevenue);
    
    // Update breakdown
    elements.investmentBreakdown.innerHTML = `
      <div class="breakdown-item">
        <span>Mensile: ${formatCurrency(calculations.totalMonthlyCost)}</span>
        <span>Una tantum: ${formatCurrency(calculations.oneTimeCost)}</span>
      </div>
    `;
    
    // Update ROI description
    const paybackText = calculations.paybackMonths <= 12 ? 
      `Rientro investimento in ${calculations.paybackMonths} mesi` :
      'Rientro investimento oltre 12 mesi';
    
    elements.roiDescription.textContent = paybackText;
    
    // Remove animation class
    setTimeout(() => {
      elements.totalInvestment.classList.remove('updating');
      elements.expectedROI.classList.remove('updating');
      elements.newClients.classList.remove('updating');
      elements.additionalRevenue.classList.remove('updating');
    }, 300);
  }, 150);
}

// Initialize chart
function initializeChart() {
  const canvas = document.getElementById('costChart');
  const ctx = canvas.getContext('2d');
  
  // Set canvas size
  canvas.width = 300;
  canvas.height = 200;
  
  costChart = { canvas, ctx };
}

// Update chart
function updateChart(breakdown) {
  const { canvas, ctx } = costChart;
  
  // Clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Filter out zero values
  const data = Object.entries(breakdown).filter(([key, value]) => value > 0);
  
  if (data.length === 0) return;
  
  // Colors for different categories
  const colors = ['#8B1538', '#DAA520', '#2F4F2F', '#B8860B', '#654321'];
  
  // Calculate total for percentages
  const total = data.reduce((sum, [key, value]) => sum + value, 0);
  
  // Chart dimensions
  const chartWidth = canvas.width - 80;
  const chartHeight = canvas.height - 60;
  const maxValue = Math.max(...data.map(([key, value]) => value));
  
  // Draw bars
  const barWidth = chartWidth / data.length - 10;
  const startX = 40;
  const startY = canvas.height - 40;
  
  data.forEach(([label, value], index) => {
    const barHeight = (value / maxValue) * chartHeight;
    const x = startX + (index * (barWidth + 10));
    const y = startY - barHeight;
    
    // Draw bar
    ctx.fillStyle = colors[index % colors.length];
    ctx.fillRect(x, y, barWidth, barHeight);
    
    // Draw value on top of bar
    ctx.fillStyle = '#333';
    ctx.font = '12px Arial';
    ctx.textAlign = 'center';
    const displayValue = value >= 1000 ? `€${Math.round(value/1000)}k` : `€${value}`;
    ctx.fillText(displayValue, x + barWidth/2, y - 5);
    
    // Draw label
    ctx.save();
    ctx.translate(x + barWidth/2, startY + 15);
    ctx.rotate(-Math.PI/4);
    ctx.font = '10px Arial';
    ctx.textAlign = 'center';
    ctx.fillText(label.substring(0, 12), 0, 0);
    ctx.restore();
  });
}

// Modal functions
function openModal() {
  elements.modal.classList.add('active');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  elements.modal.classList.remove('active');
  document.body.style.overflow = '';
}

function handleFormSubmit(e) {
  e.preventDefault();
  
  const formData = new FormData(elements.quoteForm);
  const data = {
    name: document.getElementById('client-name').value,
    email: document.getElementById('client-email').value,
    phone: document.getElementById('client-phone').value,
    message: document.getElementById('client-message').value,
    parameters: currentParams,
    calculations: calculateMetrics()
  };
  
  // Simulate form submission
  const submitBtn = elements.quoteForm.querySelector('button[type="submit"]');
  const originalText = submitBtn.textContent;
  
  submitBtn.textContent = 'Invio in corso...';
  submitBtn.disabled = true;
  
  setTimeout(() => {
    // Show success message
    const successMessage = document.createElement('div');
    successMessage.className = 'form-success';
    successMessage.textContent = 'Richiesta inviata con successo! Ti ricontatteremo entro 24 ore.';
    
    elements.quoteForm.parentNode.insertBefore(successMessage, elements.quoteForm);
    
    // Reset form
    elements.quoteForm.reset();
    
    setTimeout(() => {
      closeModal();
      successMessage.remove();
      submitBtn.textContent = originalText;
      submitBtn.disabled = false;
    }, 2000);
  }, 1500);
}

// Utility functions
function formatCurrency(amount) {
  return new Intl.NumberFormat('it-IT', {
    style: 'currency',
    currency: 'EUR',
    minimumFractionDigits: 0,
    maximumFractionDigits: 0
  }).format(amount);
}

// Add some interactive enhancements
document.addEventListener('DOMContentLoaded', function() {
  // Add hover effects to result cards
  const resultCards = document.querySelectorAll('.result-card');
  resultCards.forEach(card => {
    card.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-4px)';
    });
    
    card.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });
  
  // Add smooth scrolling for better UX
  const smoothScroll = (target) => {
    target.scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    });
  };
  
  // Add keyboard navigation for sliders
  const sliders = document.querySelectorAll('.slider');
  sliders.forEach(slider => {
    slider.addEventListener('keydown', function(e) {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
        setTimeout(() => {
          this.dispatchEvent(new Event('input'));
        }, 10);
      }
    });
  });
  
  // Add loading states for better perceived performance
  const addLoadingState = (element) => {
    element.classList.add('loading');
    setTimeout(() => {
      element.classList.remove('loading');
    }, 200);
  };
  
  // Enhance form validation
  const inputs = elements.quoteForm.querySelectorAll('input[required]');
  inputs.forEach(input => {
    input.addEventListener('blur', function() {
      if (this.value.trim() === '') {
        this.style.borderColor = '#C0152F';
      } else {
        this.style.borderColor = '';
      }
    });
    
    input.addEventListener('input', function() {
      if (this.style.borderColor === 'rgb(192, 21, 47)') {
        this.style.borderColor = '';
      }
    });
  });
});

// Add comparison feature
function showComparison() {
  const current = calculateMetrics();
  const market = appData.competitor_data;
  
  alert(`
Confronto con la media di mercato:

Il tuo piano:
• Budget: ${formatCurrency(current.totalInvestment)}
• ROI: ${current.expectedROI}%
• Nuovi clienti/mese: ${current.newClientsMonth}

Media mercato:
• Budget: ${formatCurrency(market.budget_medio_mercato * 6)}
• ROI: ${market.roi_medio_mercato}%
• Nuovi clienti/mese: ${market.clienti_medi_mercato}

${current.expectedROI > market.roi_medio_mercato ? 
  '✅ Il tuo piano supera la media di mercato!' : 
  '⚠️ Considera di ottimizzare il piano per migliorare il ROI'}
  `);
}

// Export functionality (simulated)
function exportToPDF() {
  const calculations = calculateMetrics();
  
  alert(`
Esportazione PDF simulata

Riepilogo preventivo:
• Investimento totale: ${formatCurrency(calculations.totalInvestment)}
• ROI atteso: ${calculations.expectedROI}%
• Nuovi clienti/mese: ${calculations.newClientsMonth}
• Fatturato aggiuntivo/anno: ${formatCurrency(calculations.annualRevenue)}
• Durata progetto: ${currentParams.projectDuration} mesi

In un'applicazione reale, qui verrebbe generato e scaricato un PDF dettagliato.
  `);
}