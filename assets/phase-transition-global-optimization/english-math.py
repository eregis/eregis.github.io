import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Label } from 'recharts';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

const StudyChoicePlots = () => {
  // Define parameters (keeping same mathematical structure)
  const t = -4.0;  
  const c = 1.0;   
  const bias_values = [0.5, 0, -0.5];  // Now represents study preference bias
  
  // Generate values for fraction of time (instead of phi)
  const fraction_values = Array.from({ length: 200 }, (_, i) => -2 + (4 * i) / 199);
  
  // Generate data for each bias value
  const generateData = (bias) => {
    return fraction_values.map(x => ({
      fraction: x,
      income: -(t * Math.pow(x, 2) + c * Math.pow(x, 4) - bias * x)
    }));
  };

  const datasets = bias_values.map(bias => generateData(bias));

  return (
    <Card className="w-full max-w-6xl">
      <CardHeader>
        <CardTitle className="text-center">
          Expected Income vs Study Choice
          <div className="text-sm mt-1">(Math ← → English)</div>
        </CardTitle>
      </CardHeader>
      <CardContent className="flex flex-wrap justify-center gap-4">
        {datasets.map((data, index) => (
          <div key={index} className="relative">
            <LineChart
              width={350}
              height={300}
              data={data}
              margin={{ top: 20, right: 30, left: 50, bottom: 30 }}
            >
              <CartesianGrid strokeDasharray="3 3" opacity={0.3} />
              <XAxis
                dataKey="fraction"
                type="number"
                domain={[-2, 2]}
                tick={{ fontSize: 12 }}
              >
                <Label value="Fraction of Time (Math ← → English)" position="bottom" offset={10} />
              </XAxis>
              <YAxis
                type="number"
                domain={[-10, 10]}
                tick={{ fontSize: 12 }}
              >
                <Label
                  value="Expected Lifetime Income"
                  angle={-90}
                  position="left"
                  offset={25}
                />
              </YAxis>
              <Tooltip
                formatter={(value) => `$${(value * 10000).toFixed(0)}`}
                labelFormatter={(value) => `Balance: ${value < 0 ? 'More Math' : 'More English'}`}
              />
              <Line
                type="monotone"
                dataKey="income"
                stroke="#2563eb"
                dot={false}
                strokeWidth={2}
              />
            </LineChart>
            <div className="absolute top-0 left-0 mt-2 ml-4 font-medium">
              Market Bias = {bias_values[index]}
            </div>
          </div>
        ))}
      </CardContent>
    </Card>
  );
};

export default StudyChoicePlots;
