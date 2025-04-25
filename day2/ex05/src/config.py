# Количество шагов для метода predict_random
NUM_OF_STEPS = 3

# Шаблон текста для отчета
REPORT_TEMPLATE = (
    "We have made {total_observations} observations from tossing a coin: "
    "{tails_count} of them were tails and {heads_count} of them were heads. "
    "The probabilities are {tails_fraction:.2f}% and {heads_fraction:.2f}%, respectively. "
    "Our forecast is that in the next {num_steps} observations we will have: "
    "{forecast_tails} tail(s) and {forecast_heads} head(s)."
)
