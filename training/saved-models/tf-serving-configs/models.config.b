model_config_list {
  config {
    name: 'my-model'
    base_path: '/saved-models/models'
    model_platform: 'tensorflow'
    model_version_policy: {
		specific: {
			versions: 2
			versions: 3
		}
	}
  }
}
