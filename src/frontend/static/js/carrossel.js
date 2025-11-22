document.addEventListener('DOMContentLoaded', () => {
    const detailContainers = document.querySelectorAll('.planeta-details');
    const visualSlides = document.querySelectorAll('.planet-slide');
    const visualCarousel = document.querySelector('.carousel-visuals');
    const carouselWrapper = document.querySelector('.carousel-visuals-wrapper');

    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');

    let currentIndex = 0;
    const totalPlanets = visualSlides.length;

    function updateCarousel() {
        if (totalPlanets === 0) return;

        const activeSlide = visualSlides[currentIndex];
        const wrapperWidth = carouselWrapper.offsetWidth;

        const activeSlideOffsetLeft = activeSlide.offsetLeft;
        const centerOfActiveSlide = activeSlideOffsetLeft + (activeSlide.offsetWidth / 2);

        const centerOfWrapper = wrapperWidth / 2;

        const translationX = centerOfWrapper - centerOfActiveSlide;

        setTimeout(() => {
            visualCarousel.style.transform = `translateX(${translationX}px)`;
        }, 10);

        visualSlides.forEach((slide, index) => {
            const planetName = slide.querySelector('h2');

            if (detailContainers[index]) {
                detailContainers[index].style.display = (index === currentIndex) ? 'flex' : 'none';
            }

            if (index === currentIndex) {
                slide.style.opacity = '1';
                slide.style.transform = 'scale(1.1)';
                if (planetName) {
                    planetName.style.opacity = '1';
                }
            } else {
                slide.style.opacity = '0.5';
                slide.style.transform = 'scale(0.8)';
                if (planetName) {
                    planetName.style.opacity = '0';
                }
            }
        });
    }

    function navigate(direction) {
        currentIndex += direction;

        if (currentIndex >= totalPlanets) {
            currentIndex = 0;
        } else if (currentIndex < 0) {
            currentIndex = totalPlanets - 1;
        }

        updateCarousel();
    }

    prevButton.addEventListener('click', () => navigate(-1));
    nextButton.addEventListener('click', () => navigate(1));

    const images = document.querySelectorAll('.planet-slide img');
    let imagesLoaded = 0;

    const imageLoadHandler = () => {
        imagesLoaded++;
        if (imagesLoaded === images.length) {
            updateCarousel();
        }
    };

    images.forEach(img => {
        if (img.complete) {
            imageLoadHandler();
        } else {
            img.addEventListener('load', imageLoadHandler);
            img.addEventListener('error', imageLoadHandler);
        }
    });

    if (images.length === 0) {
        updateCarousel();
    }

    window.addEventListener('resize', updateCarousel);
});