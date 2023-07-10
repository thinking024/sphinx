def fun(x: int, y: int) -> int:
    """
    Args:
        x (int): First number
        y (int): Second number

    Returns:
        int: Sum of x and y
    """
    return x + y


class Trainer():
    """
    Trainer class for training the model
    """
    def __init__(self, device='cpu') -> None:
        """
        Args:
            device (str): Device to train the model on. Defaults to 'cpu'.
        """
        self.device = device

    def train():
        """
        Train the model
        """
        print('Training...')
