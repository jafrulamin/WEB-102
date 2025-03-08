import { useState } from 'react';
import './App.css';


const flashcards = [
  { question: 'Which city is famous for the Eiffel Tower and its romantic ambiance?', answer: 'Paris, France' },
  { question: 'Which city is renowned for its ancient ruins like the Colosseum and rich history?', answer: 'Rome, Italy' },
  { question: 'Which city is known for its towering skyscrapers and bustling financial district?', answer: 'New York City, USA' },
  { question: 'Which city is celebrated for its picturesque canals and gondola rides?', answer: 'Venice, Italy' },
  { question: 'Which city is famous for its iconic Opera House and Harbour Bridge?', answer: 'Sydney, Australia' },
  { question: 'Which city is known for its vibrant art scene, architecture, and tapas culture?', answer: 'Barcelona, Spain' },
  { question: 'Which city is famous for its bustling street markets and ornate temples?', answer: 'Bangkok, Thailand' },
  { question: 'Which city is recognized for its charming canals, bicycles, and creative spirit?', answer: 'Amsterdam, Netherlands' },
  { question: 'Which city is celebrated for its blend of tradition and cutting-edge technology?', answer: 'Tokyo, Japan' },
  { question: 'Which city is famous for its royal heritage, iconic clock tower, and cultural significance?', answer: 'London, United Kingdom' },
];


function App() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);

  
  const currentCard = flashcards[currentIndex];

  const handleCardClick = () => {
    setIsFlipped(prev => !prev);
  };

  const handleNextCard = () => {
    setCurrentIndex((prevIndex) => (prevIndex + 1) % flashcards.length);
    setIsFlipped(false); 
  };

  const handlePrevCard = () => {
    setCurrentIndex((prevIndex) => (prevIndex - 1 + flashcards.length) % flashcards.length);
    setIsFlipped(false); 
  };

  return (
    <div className="App">
      <header>
        <h1>Famous Cities Flashcards: Discover Global Landmarks</h1>
        <p>A simple app to help you study and learn about famous cities and their remarkable landmarks</p>
        <p>Total Cards: {flashcards.length}</p>
      </header>

      <div className="card-container" onClick={handleCardClick}>
        <div className={`card ${isFlipped ? 'flipped' : ''}`}>
          <div className="card-face card-front">
            {currentCard.question}
          </div>
          <div className="card-face card-back">
            {currentCard.answer}
          </div>
        </div>
      </div>

      <div className="navigation">
        <button onClick={handlePrevCard}>&larr;</button>
        <button onClick={handleNextCard}>&rarr;</button>
      </div>
    </div>
  );
}

export default App;
