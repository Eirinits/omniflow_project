import omniflow_project.core.network as network
import omniflow_project._inputs.resources as resources

import pandas as pd

__all__ = ['TestAlgorithms']


class TestAlgorithms:

    def test_complete_connection(self, ca1_network: pd.DataFrame):

        genes = ['SRC', 'NOTCH1', 'PTK2']
        res = resources.Resources()
        res.add_database(ca1_network)
        net = network.Network(genes, res)

        net.complete_connection(
            maxlen = 6,
            k_mean = 'tight',
            only_signed = True,
            connect_node_when_first_introduced = True,
            consensus = True,
        )

        assert net.edges.shape == (12, 5)