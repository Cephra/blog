+++
title = "I Love Functional Programming"
date = 2024-06-18 18:02:05+00:00
summary = "This blog post showcases an example of using functional programming principles in TypeScript to process data efficiently and scalably. It demonstrates the use of mapping, filtering, and reducing concepts to calculate cumulative sums from multiple repositories without explicit loops or mutable state."
+++
I just love functional programming. In this code snippet, we see a great example of using functional programming principles to process data in a efficient and scalable way.

The code is using TypeScript to query two repositories: `meterRepository` and `valueRepository`. It's retrieving meters by type, values for each meter within a specific timestamp range, and then processing the data to calculate cumulative sums. The result is an array of processed values, which can be used for further analysis or visualization.

The code uses several functional programming concepts, such as:

* Mapping: to transform the `metersByType` array into an array of objects with additional properties (`creationDate`, `firstValue`, and `lastValue`)
* Filtering: to extract values for each meter from the `valuesByMeterType` array
* Reducing: to calculate cumulative sums by summing up values from previous meters

These concepts allow us to process the data in a declarative way, without having to use explicit loops or mutable state. The resulting code is not only more concise but also easier to reason about and maintain.

The use of functional programming also enables better composability of the code. We can break down complex processing into smaller, reusable functions that can be composed together to achieve the desired result.

In this specific example, we're able to efficiently calculate cumulative sums for each meter by leveraging the `reduce` method and the `slice` method to process the data in a single pass. This approach avoids the need for explicit loops or recursive functions, making it more efficient and easier to understand.

### Code snippet

```typescript
const metersByType = await this.meterRepository.find({
  where: { meterTypeId },
  fields: ['id'],
});
const valuesByMeterType = await this.valueRepository.find({
  where: {
    meterId: {
      inq: metersByType.map(m => m.id as number),
    },
    timestamp: {
      between: [
        new Date(from ?? 0).toISOString(),
        (to ? new Date(to) : new Date()).toISOString(),
      ],
    },
  },
  fields: ['value', 'timestamp', 'meterId'],
  order: ['timestamp asc'],
});
const sortedMetersByType = metersByType
  .map(m => {
    const firstValue = valuesByMeterType.find(v => v.meterId === m.id);
    const lastValue = valuesByMeterType.findLast(v => v.meterId === m.id);

    const creationDate = new Date(firstValue?.timestamp ?? 0);

    return new MeterWithStats({
      ...m,
      creationDate,
      firstValue: firstValue?.value ?? 0,
      lastValue: lastValue?.value ?? 0,
    });
  })
  .sort((a, b) => {
    return (
      (a.creationDate as Date).getTime() -
      (b.creationDate as Date).getTime()
    );
  });
const sortedValues = sortedMetersByType
  .map((meter, i) => {
    const valuesForMeter = valuesByMeterType
      .filter(v => v.meterId === meter.id)
      .map(v => {
        const cumSum = sortedMetersByType
          .slice(0, i)
          .map(m => ((m.lastValue ?? 0) - (m.firstValue ?? 0)))
          .reduce((acc, m) => m + acc, 0);
        const firstValueOfCurrentMeter = meter.firstValue ?? 0;

        v.value = v.value - firstValueOfCurrentMeter + cumSum;

        return v;
      });

    return valuesForMeter;
  })
  .flat();

return sortedValues;
```