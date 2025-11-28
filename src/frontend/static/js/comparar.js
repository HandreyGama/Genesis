document.addEventListener('DOMContentLoaded', function() {

    if (!window.planetaData || window.planetaData.length === 0) {
        console.warn('Nenhum dado de planeta encontrado para o gráfico.');
        return;
    }

    const ctx = document.getElementById('planetRadarChart').getContext('2d');

    const neonColors = [
        { border: 'rgba(0, 195, 255, 1)',   bg: 'rgba(0, 195, 255, 0.25)' }, // Cyan
        { border: 'rgba(255, 99, 132, 1)',   bg: 'rgba(255, 99, 132, 0.25)' }, // Pink
        { border: 'rgba(255, 206, 86, 1)',   bg: 'rgba(255, 206, 86, 0.25)' }, // Yellow
        { border: 'rgba(46, 204, 113, 1)',   bg: 'rgba(46, 204, 113, 0.25)' }, // Lime Green
        { border: 'rgba(157, 0, 255, 1)',    bg: 'rgba(157, 0, 255, 0.25)' }   // Purple
    ];

    const datasets = window.planetaData.map((planeta, index) => {
        const color = neonColors[index % neonColors.length];

        return {
            label: planeta.nome,
            data: [
                planeta.raio,
                planeta.massa,
                planeta.gravidade,
                planeta.esi
            ],
            backgroundColor: color.bg,
            borderColor: color.border,
            borderWidth: 2,
            pointBackgroundColor: '#fff',
            pointBorderColor: color.border,
            pointHoverBackgroundColor: color.border,
            pointHoverBorderColor: '#fff',
            fill: true
        };
    });

    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: [
                'Raio (R⊕)',
                'Massa (M⊕)',
                'Gravidade (g)',
                'Habitabilidade (Escala 5.0)'
            ],
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            elements: {
                line: {
                    tension: 0.3 //
                }
            },
            scales: {
                r: {
                    angleLines: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    },
                    grid: {
                        color: 'rgba(255, 255, 255, 0.1)'
                    },
                    pointLabels: {
                        color: '#e0e0e0',
                        font: {
                            family: '"Poppins", sans-serif',
                            size: 14,
                            weight: '600'
                        }
                    },
                    ticks: {
                        backdropColor: 'transparent',
                        color: 'rgba(255, 255, 255, 0.5)',
                        showLabelBackdrop: false
                    },
                    suggestedMin: 0,
                    // suggestedMax: 5 // Pode descomentar para fixar a escala se quiser
                }
            },
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        color: '#fff',
                        font: {
                            family: '"Poppins", sans-serif',
                            size: 14
                        },
                        padding: 20
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    titleFont: { family: '"Poppins", sans-serif', size: 14 },
                    bodyFont: { family: '"Poppins", sans-serif', size: 13 },
                    padding: 10,
                    cornerRadius: 8,
                    displayColors: true
                }
            },
            animation: {
                duration: 1500, //
                easing: 'easeOutQuart'
            }
        }
    });
});
