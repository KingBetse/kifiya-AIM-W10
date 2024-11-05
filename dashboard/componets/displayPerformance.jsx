const PerformanceMetrics = () => {
    const [metrics, setMetrics] = useState({});

    useEffect(() => {
        const fetchMetrics = async () => {
            const response = await axios.get('http://localhost:5000/api/performance');
            setMetrics(response.data);
        };
        fetchMetrics();
    }, []);

    return (
        <div>
            <h3>Model Performance Metrics</h3>
            <p>Mean Absolute Error (MAE): {metrics.MAE}</p>
            <p>Mean Squared Error (MSE): {metrics.MSE}</p>
            <p>R-squared: {metrics.R_squared}</p>
        </div>
    );
};