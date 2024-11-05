// src/App.js
import React from 'react';
import PriceChart from './components/PriceChart';
import CorrelationChart from './components/CorrelationChart';
import PerformanceMetrics from './components/PerformanceMetrics';
import PredictPrice from './components/PredictPrice';

function App() {
    return (
        <div className="App">
            <h1>Brent Oil Price Dashboard</h1>
            <PriceChart />
            <CorrelationChart />
            <PerformanceMetrics />
            <PredictPrice />
        </div>
    );
}

export default App;