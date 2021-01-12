CLUSTER_CONF_HOME=kafka-environment/cluster

create-cluster:
	kind create cluster --config $(CLUSTER_CONF_HOME)/kafka-cluster-config.yaml --name kafka-cluster
