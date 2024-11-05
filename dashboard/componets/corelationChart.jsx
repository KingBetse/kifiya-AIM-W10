const CorrelationChart = ({ data }) => {
    return (
        <LineChart width={600} height={300} data={data}>
            <XAxis dataKey="date" />
            <YAxis />
            <Tooltip />
            <CartesianGrid strokeDasharray="3 3" />
            <Line type="monotone" dataKey="GDP_Billion" stroke="#82ca9d" />
            <Line type="monotone" dataKey="Unemployment_Rate" stroke="#ffc658" />
            <Line type="monotone" dataKey="CPI" stroke="#ff7300" />
        </LineChart>
    );
};